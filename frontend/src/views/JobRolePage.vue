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
                        <RouterLink to="/manager">Job Role</RouterLink>
                    </li> 
                    <li>
                        {{role.roleName}}
                    </li>
                </ul>
            </div>
            <div class="grid grid-cols-2 my-4">
                <!-- Role Name -->
                <p class="text-3xl font-bold underline underline-offset-8">
                    {{role.roleName}}
                </p>
                <!-- Edit button -->
                <button @click="handleEditClick(role.roleName)" class="btn btn-circle place-self-end">
                    <svg class="w-4 h-4 fill-current" viewBox="0 0 20 20"><path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z"></path></svg>
                </button>
            </div>
            <!-- Role Desc -->
            <div class="space-y-2 my-4 w-4/6">
                <p class="font-medium text-lg">
                    Job Role Description
                </p>
                <p>
                    {{role.roleDesc}}
                </p>
            </div>
            <!-- Skills -->
            <div class="space-y-3 my-4">
                <p class="text-2xl font-medium">
                    Skills
                </p>
                <!-- Skills component -->
                <div v-if="noSkills != ''">
                    {{noSkills}}
                </div>
                <div v-else class="bg-gray-700 rounded-lg my-6 p-8" v-for="(skillDetails, skillName) in role.coursesBySkillName" :key="skillName">
                    <!-- Skill -->
                    <div class="font-medium text-lg mb-5">
                        {{skillName}}
                    </div>
                    <!-- Courses -->
                    <div v-if="noCourses">
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
import { getRoleDetails, getSkillsByRole, getCoursesBySkill } from "@/endpoint/endpoint.js";

const router = useRouter()
const route = useRoute()
const roleStore = useRoleStore()

// from params
const roleName = route.params.jobRoleName

const role = reactive({
    roleName: '',
    roleID: '',
    roleDesc: '',
    coursesBySkillName: {}
})

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
        role.roleName = roleDetails.Role_Name
        role.roleID = roleDetails.Role_ID
        role.roleDesc = roleDetails.Role_Desc

        // get skills with role ID
        try {
            const roleSkills = await getSkillsByRole(roleDetails.Role_ID)
            // get courses with each skill ID
            try {
                for (var skill of roleSkills) {
                    // fk error here
                    const skillCourses = await getCoursesBySkill(skill.Skill_ID)
                    for (var course of skillCourses) {
                        // skillName exist in object
                        if (role.coursesBySkillName[skill.Skill_Name]) {
                            role.coursesBySkillName[skill.Skill_Name].courses[course.Course_Name] = course
                        // skillName does not exist in object
                        } else {
                            role.coursesBySkillName[skill.Skill_Name] = {
                                'skillID': skill.Skill_ID,
                                'courses': {}
                            }
                            role.coursesBySkillName[skill.Skill_Name].courses[course.Course_Name] = course
                        }
                    }
                }
            }
            catch (err) {
                console.log(err.message);
                // noCourses.value = err.message
            }

        }
        catch (err) {
            noSkills.value = err.message
        }

        // store role in global store to be use by edit job role page
        roleStore.storeRole(role.roleName, role.roleID, role.roleDesc, role.coursesBySkillName)

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
    courseModal.courseDesc = role.coursesBySkillName[skillName].courses[courseName].Course_Desc
}

</script>

<style scoped>
</style>