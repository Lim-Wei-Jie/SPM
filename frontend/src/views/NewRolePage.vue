<template>
<!-- eslint-disable -->
<div>
    <NavBar/>
    <div class="container mx-auto my-8">
        <div v-if="loading">

            <!-- Back button -->
            <div>
                <RouterLink to="/manager">
                    <button class="btn btn-circle"  @click="handleBack">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h10a8 8 0 018 8v2M3 10l6 6m-6-6l6-6" />
                        </svg>
                    </button>
                </RouterLink>
            </div>

            <p class="text-3xl my-8"> Add Job Role </p>

            <!-- Form component -->
            <form class="form-control space-y-6" @submit.prevent="handleAddRole">
            
                <!-- Role name input -->
                <div class="space-y-2">
                    <h3 class="font-medium text-lg">Job Role Name</h3>
                    <input type="text" placeholder="Job Role Name" v-model="roleStore.role.roleName" class="input input-bordered w-3/6 text-2xl">
                </div>

                <!-- Role desc input -->
                <div class="space-y-2 w-4/6">
                    <p class="font-medium text-lg">
                        Job Role Description
                    </p>
                    <input type="text" placeholder="Job Role Description" v-model="roleStore.role.roleDesc" class="input input-bordered w-full">
                </div>

                <!-- Role skills -->
                <div class="space-y-3">
                    <p class="font-medium text-lg"> Skills </p>
                    <!-- Skills component -->
                    <div class="grid grid-cols-4 gap-6 bg-gray-700 rounded-lg my-6 p-8">
                        <!-- Skill -->
                        <div class="flex justify-evenly" v-for="(skillDetails, skillName) in roleStore.role.coursesBySkillName" :key="skillName">
                            <div class="text-center bg-gray-800 rounded-lg w-11/12 p-3 relative">
                                {{ skillName }}
                                <!-- Remove skill button -->
                                <label for="remove-modal" class="btn modal-button btn-xs btn-circle btn-error btn-outline absolute right-0 top-0" @click="handleRemoveSkill(skillName)">
                                    <svg class="h-3 w-3" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                                    </svg>
                                </label>
                                <!-- Modal pop-up -->
                                <input type="checkbox" id="remove-modal" class="modal-toggle"/>
                                <label for="remove-modal" class="modal cursor-default">
                                    <label class="modal-box relative space-y-8">
                                        <p class="text-lg">
                                            Are you sure you want to remove skill:
                                            <section class="text-xl mt-3">
                                                {{ removeModal.skillName }}
                                            </section>
                                        </p>
                                        <!-- Confirm + cancel buttons -->
                                        <div class="grid grid-cols-2 gap-6">
                                            <div class="flex justify-end">
                                                <label for="remove-modal" class="btn btn-sm btn-error btn-outline w-3/5" @click="confirmRemoveSkill(removeModal.skillName)">
                                                    Confirm
                                                </label>
                                            </div>
                                            <div class="flex justify-start">
                                                <label for="remove-modal" class="btn btn-sm btn-outline w-3/5">
                                                    Cancel
                                                </label>
                                            </div>
                                        </div>
                                    </label>
                                </label>
                            </div>
                        </div>

                        <!-- Add skill button -->
                        <label for="add-modal" class="flex justify-evenly">
                            <div class="btn btn-outline border-dashed rounded-lg w-11/12 h-full" @click="handleAddSkill">
                                Add New Skills
                            </div>
                        </label>
                        <!-- Modal pop-up -->
                        <input type="checkbox" id="add-modal" class="modal-toggle"/>
                        <div class="modal">
                            <div class="modal-box space-y-8">
                                <!-- All skills in checkbox 
                                    (assigned skills not shown) -->
                                <ul class="space-y-3">
                                    <li v-for="skill of addModal.skillArr" class="bg-gray-800 hover:shadow-lg hover:bg-black rounded-lg">
                                        <label :for="skill.Skill_ID">
                                            <div class="flex justify-between cursor-pointer p-4">
                                                <p class="font-medium">
                                                    {{skill.Skill_Name}}
                                                </p>
                                                <input type="checkbox" class="checkbox" v-model="addModal.selectedSkills"  :value="skill" :id="skill.Skill_ID"/>
                                            </div>
                                        </label>
                                    </li>
                                </ul>
                                
                                <!-- Add + cancel buttons -->
                                <div class="grid grid-cols-2 gap-6">
                                    <div class="flex justify-end">
                                        <label for="add-modal" class="btn btn-sm w-3/5" @click="confirmAddSkill">
                                            Add
                                        </label>
                                    </div>
                                    <div class="flex justify-start">
                                        <label for="add-modal" class="btn btn-sm btn-outline w-3/5">
                                            Cancel
                                        </label>
                                    </div>
                                </div>

                            </div>
                        </div>

                    </div>
                </div>

                <!-- Add button -->
                <button class="btn w-1/5" type="submit">Add Role</button>
                <!-- Cancel button -->
                <div>
                    <RouterLink to="/manager">
                        <div class="btn btn-outline btn-error w-1/5" @click="handleBack">
                            Cancel
                        </div>
                    </RouterLink>
                </div>
            
            </form>

        </div>

        <div v-else-if="error !== ''">
            {{ error }}
        </div>
        
        <div v-else>
            <button class="btn loading">loading</button>
        </div>

    </div>

</div>

</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
import { reactive, ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useRoleStore, useAssignSkillsStore } from '@/store/index.js'
import { getAllSkills, getCoursesBySkill, createRole } from '@/endpoint/endpoint.js'

const router = useRouter()
const route = useRoute()
const roleStore = useRoleStore()
const assignSkillsStore = useAssignSkillsStore()

const removeModal = reactive({
    skillName: '',
})

const addModal = reactive({
    skillArr: [],
    selectedSkills: [],
})

const addSkillsIDArr = ref(assignSkillsStore.assignSkills.addSkillsIDArr)

const loading = ref(true);
const error = ref('');

// reset assignSkillsStore when exit edit role page (using back or cancel btn)
function handleBack() {
    assignSkillsStore.assignSkills.addSkillsIDArr = []
}

function handleRemoveSkill(skillName) {
    removeModal.skillName = skillName
}

function confirmRemoveSkill(skillName) {
    // store Skill ID/s in an array for API call when submit form
    const skillID = (roleStore.role.coursesBySkillName[skillName].skillID).toString()
    // check if skill id in addSkillsIDArr
    if (addSkillsIDArr.value.includes(skillID)) {
        const index = addSkillsIDArr.value.indexOf(skillID)
        addSkillsIDArr.value.splice(index, 1)
    } else {
        // pass
    }

    // removing skill key from coursesBySkillName object in pinia store only
    delete roleStore.role.coursesBySkillName[skillName]
}

async function handleAddSkill() {
    // get all skills
    try {
        const allSkills = await getAllSkills()
        addModal.skillArr = []
        for (var skill of allSkills) {
            if (!(skill.Skill_Name in roleStore.role.coursesBySkillName)) {
                addModal.skillArr.push(skill)
            }
        }
        // add to roleStore

    }
    catch (err) {
        // error.value = err
        console.log(err);
    }
}

async function confirmAddSkill() {
    for (var skill of addModal.selectedSkills) {
        let skillCourses = null
        try {
            skillCourses = await getCoursesBySkill(skill.Skill_ID)
        }
        catch (err) {
            error.value = err
        }

        // add skill to role store
        roleStore.role.coursesBySkillName[skill.Skill_Name] = {
            'skillID': skill.Skill_ID,
            'courses': {}
        }

        if (skillCourses) {
            // if have courses assigned to skill
            for (var course of skillCourses) {
                roleStore.role.coursesBySkillName[skill.Skill_Name].courses[course.Course_Name] = course
            }
        } else {
            // if no courses assigned to skill
            // pass
        }

        const skillID = (skill.Skill_ID).toString()
        addSkillsIDArr.value.push(skillID)

    }

    // reset modal selected skills
    addModal.selectedSkills = []
}

async function handleAddRole() {
    try {
        const addedRole = await createRole(roleStore.role, addSkillsIDArr.value)
        handleBack()
        router.push({
            name: 'manager',
        })
    }
    catch (err) {
        // error.value = err
        console.log(err);
    }
}

</script>

<style scoped>
</style>