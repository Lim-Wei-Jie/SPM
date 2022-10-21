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
                        {{roleName}}
                    </li>
                </ul>
            </div>
            <div class="grid grid-cols-2 my-4">
                <!-- Role Name -->
                <p class="text-3xl font-bold underline underline-offset-8">
                    {{roleName}}
                </p>
                <!-- Edit button -->
                <button @click="handleEditClick(roleName)" class="btn btn-circle place-self-end">
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
                <div class="bg-gray-700 rounded-lg my-6 p-8" v-for="(courseArr, skill) in role.coursesBySkillName" :key="skill">
                    <!-- Skill -->
                    <div class="font-medium text-lg mb-5">
                        {{skill}}
                    </div>
                    <!-- Courses -->
                    <div class="grid grid-cols-3 gap-6">
                        <div class="flex justify-evenly" v-for="courseName of courseArr">
                            <!-- Course Modal component -->
                            <label for="course-modal" class="btn modal-button bg-gray-800 rounded-lg w-11/12" @click="handleCourseClick(courseName)">
                                {{courseName}}
                            </label>
                            <!-- Modal pop-up -->
                            <input type="checkbox" id="course-modal" class="modal-toggle"/>
                            <label for="course-modal" class="modal cursor-default">
                                <label class="modal-box relative" for="">
                                    <label for="course-modal" class="btn btn-sm btn-circle absolute right-2 top-2">✕</label>
                                    <!-- Course name -->
                                    <div class="m-4">
                                        <p class="text-2xl font-bold underline underline-offset-8">
                                            {{course.courseName}}
                                        </p>
                                    </div>
                                    <!-- Course desc -->
                                    <div class="m-4 w-4/6">
                                        <p class="font-medium text-lg">
                                            {{course.courseDesc}}
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
            Loading...
        </div>

    </div>
    
</div>

</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
// import Breadcrumb from '@/components/Breadcrumb.vue'
import { reactive, ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { getRoleDetails, getSkillsByRole, getCoursesBySkill, getCourseDetails } from "@/endpoint/endpoint.js";

const router = useRouter()
const route = useRoute()

// from params
const roleName = route.params.jobRoleName

const role = reactive({
    roleDesc: '',
    roleID: '',
    coursesBySkillName: {} // key = skill name, value = course name
})

const course = reactive({
    courseName: '',
    courseDesc: ''
})

const loading = ref(false)
const error = ref('')

;(async() => {
    try {
        // get role name, ID, and description
        const roleDetails = await getRoleDetails(roleName)
        role.roleDesc = roleDetails.Role_Desc
        role.roleID = roleDetails.Role_ID

        // get skills with role ID
        const roleSkills = await getSkillsByRole(roleDetails.Role_ID)

        // get courses with each skill ID
        for (var skill of roleSkills) {
            const skillCourses = await getCoursesBySkill(skill.Skill_id)
            for (var course of skillCourses) {
                // check if skillName exist in object
                if (role.coursesBySkillName[skill.Skill_name]) {
                    role.coursesBySkillName[skill.Skill_name].push(course.Course_Name)
                } else {
                    role.coursesBySkillName[skill.Skill_name] = [course.Course_Name]
                }
            }
        }

        // after all API calls made
        loading.value = true
    }
    catch(err) {
        error.value = err
        console.log(err);
    }
})();

function handleEditClick(roleDetailsName) {
    router.push({
        name: 'editRole',
        params: {
            jobRoleName: roleDetailsName
        }
    })
}

async function handleCourseClick(courseName) {
    course.courseName = ''
    course.courseDesc = ''
    try {
        const courseDetails = await getCourseDetails(courseName)
        course.courseName = courseName
        course.courseDesc = courseDetails.Course_Desc
    } 
    catch (err) {
        error.value = err
        console.log(err);
    }
}

</script>

<style scoped>
</style>