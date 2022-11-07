<template>
<!-- eslint-disable -->
<div>
    <NavBar/>
    <div class="container mx-auto my-8">
        <div v-if="loading">
            <!-- Breadcrumbs component -->
            <div class="text-sm breadcrumbs">
                <ul>
                    <li>
                        <RouterLink to="/login">Home</RouterLink>
                    </li>
                    <li>
                        <RouterLink to="/manager">Job Roles</RouterLink>
                    </li> 
                    <li>
                        {{roleStore.role.roleName}}
                    </li>
                </ul>
            </div>

            <!-- Back button -->
            <div class="my-8">
                <RouterLink to="/manager">
                    <button class="btn btn-circle">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h10a8 8 0 018 8v2M3 10l6 6m-6-6l6-6" />
                        </svg>
                    </button>
                </RouterLink>
            </div>

            <div class="grid grid-cols-2">
                <!-- Role Name -->
                <p class="text-3xl font-bold underline underline-offset-8">
                    {{roleStore.role.roleName}}
                </p>
                <div class="flex justify-end space-x-2">
                    <!-- Edit button -->
                    <button @click="handleEditClick(roleStore.role.roleName)" class="btn btn-circle">
                        <svg class="w-4 h-4 fill-current" viewBox="0 0 20 20"><path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z"></path></svg>
                    </button>
                    <!-- Delete button -->
                    <label for="delete-modal" @click="handleDeleteRole(roleStore.role.roleID)" class="btn btn-circle">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
                        </svg>
                    </label>
                </div>
            </div>
            
            <!-- Role Desc -->
            <div class="space-y-2 my-4 w-4/6">
                <p class="font-medium text-lg">
                    Job Role Description
                </p>
                <p>
                    {{roleStore.role.roleDesc}}
                </p>
            </div>
            <!-- Skills -->
            <div class="space-y-3 my-4">
                <p class="text-2xl font-medium">
                    Skills
                </p>
                <!-- Skills component -->
                <div v-if="noSkills">
                    {{noSkills}}
                </div>
                <div v-else class="bg-gray-700 rounded-lg my-6 p-8" v-for="(skillDetails, skillName) in roleStore.role.coursesBySkillName" :key="skillName">
                    <!-- Skill -->
                    <div class="font-medium text-lg mb-5 text-white">
                        {{skillName}}
                    </div>
                    <!-- Courses -->
                    <div class="text-white" v-if="Object.keys(roleStore.role.coursesBySkillName[skillName].courses).length === 0">
                        {{noCourses}}
                    </div>
                    <div v-else class="grid grid-cols-3 gap-6">
                        <div class="flex justify-evenly" v-for="course of skillDetails.courses">
                            <!-- Course Modal component -->
                            <label for="course-modal" class="btn modal-button bg-gray-800 rounded-lg w-11/12" @click="handleCourseClick(skillName, course.Course_Name)">
                                {{course.Course_Name}}
                            </label>
                            <!-- Modal pop-up -->
                            <input type="checkbox" id="course-modal" class="modal-toggle"/>
                            <label for="course-modal" class="modal cursor-default">
                                <label class="modal-box relative" for="">
                                    <label for="course-modal" class="btn btn-sm btn-circle absolute right-2 top-2">✕</label>
                                    <!-- Course name -->
                                    <div class="m-4">
                                        <p class="text-2xl font-bold underline underline-offset-8">
                                            {{courseModal.courseName}}
                                        </p>
                                    </div>
                                    <!-- Course desc -->
                                    <div class="m-4 w-4/6">
                                        <p class="font-medium text-lg">
                                            {{courseModal.courseDesc}}
                                        </p>
                                    </div>
                                </label>
                            </label>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Delete modal -->
            <input type="checkbox" id="delete-modal" class="modal-toggle" />
            <label for="delete-modal" class="modal cursor-default">
                <label class="modal-box relative">
                    <div class="text-center">
                        <section class="text-xl mt-3">
                            {{ roleStore.role.roleName }} successfully deleted
                        </section>
                        <label for="delete-modal" class="btn w-1/5 mt-5" @click="handleRedirect">
                            Close
                        </label>
                    </div>
                </label>
            </label>

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
// import Breadcrumb from '@/components/Breadcrumb.vue'
import { reactive, ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useRoleStore } from '@/store/index.js'
import { getRoleDetails, getSkillsByRole, getCoursesBySkill, deleteRole } from "@/endpoint/endpoint.js";

const router = useRouter()
const route = useRoute()
const roleStore = useRoleStore()

// from params
const roleName = route.params.jobRoleName

// const role = reactive({
//     roleName: '',
//     roleID: '',
//     roleDesc: '',
//     coursesBySkillName: {}
// })

const courseModal = reactive({
    courseName: '',
    courseDesc: ''
})

const loading = ref(false)
const noSkills = ref('');
const noCourses = ref('');
const error = ref(null)

;(async() => {
    try {
        // get role name, ID, and description
        const roleDetails = await getRoleDetails(roleName)
        roleStore.role.roleName = roleDetails.Role_Name
        roleStore.role.roleID = roleDetails.Role_ID
        roleStore.role.roleDesc = roleDetails.Role_Desc

        // get skills with role ID
        try {
            roleStore.role.coursesBySkillName = {}
            const roleSkills = await getSkillsByRole(roleDetails.Role_ID)
            // get courses with each skill ID
            for (var skill of roleSkills) {
                let skillCourses = null
                try {
                    skillCourses = await getCoursesBySkill(skill.Skill_ID)
                }
                catch (err) {
                    noCourses.value = err.message
                }

                // add skill to role store
                roleStore.role.coursesBySkillName[skill.Skill_Name] = {
                    'skillID': skill.Skill_ID,
                    'courses': {}
                }

                if (skillCourses) {
                    // if there are courses assigned to skill
                    for (var course of skillCourses) {
                        roleStore.role.coursesBySkillName[skill.Skill_Name].courses[course.Course_Name] = course
                    }
                } else {
                    // if there are no courses assigned to skill
                    // pass
                }
            }
        }
        catch (err) {
            // no skills assigned
            roleStore.role.coursesBySkillName = {}
            noSkills.value = err.message
        }

        // after all API calls made
        loading.value = true
    }
    catch(err) {
        error.value = err
        console.log(err);
    }
})();

function handleEditClick(roleName) {
    router.push({
        name: 'editRole',
        params: {
            jobRoleName: roleName
        }
    })
}

function handleCourseClick(skillName, courseName) {
    courseModal.courseName = courseName
    courseModal.courseDesc = roleStore.role.coursesBySkillName[skillName].courses[courseName].Course_Desc
}

async function handleDeleteRole(roleID) {
    try {
        const deletedRole = await deleteRole(roleID)
    }
    catch (err) {
        console.log(err);
    }
}

function handleRedirect() {
    router.push({
        name: 'manager'
    })
}

</script>

<style scoped>
</style>