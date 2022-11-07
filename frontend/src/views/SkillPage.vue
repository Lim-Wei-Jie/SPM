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
                        <RouterLink to="/hr">Skill</RouterLink>
                    </li> 
                    <li>
                        {{skill.skillName}}
                    </li>
                </ul>
            </div>
            <div class="grid grid-cols-3 my-4">
                <!-- Role Name -->
                <p class="text-3xl font-bold underline underline-offset-8">
                    {{skill.skillName}}
                </p>
                <div class="flex justify-end space-x-2">
                    <!-- Edit button -->
                    <button @click="handleEditClick(skill.skillName)" class="btn btn-circle place-self-end">
                        <svg class="w-4 h-4 fill-current" viewBox="0 0 20 20"><path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z"></path></svg>
                    </button>
                    <!-- Delete button -->
                    <label for="delete-skill-modal"  @click="handleDeleteSkill()" class="btn btn-circle place-self-end">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
                            </svg>
                        </label>
                        <!-- Modal pop-up -->
                        <input type="checkbox" id="delete-skill-modal" class="modal-toggle"/>
                                        <label for="delete-skill-modal" class="modal cursor-default">
                                            <label class="modal-box relative space-y-8">
                                                <div v-if="noErr">
                                                    <!-- Ok button -->
                                                    <p class="text-lg">
                                                        <RouterLink :to="`/hr`">
                                                            <section class="text-xl mt-3">
                                                                {{ skill.skillName }} has been deleted
                                                            </section>
                                                            <div class="btn btn-sm flex justify-end">    
                                                                Ok
                                                            </div> 
                                                        </RouterLink>
                                                    </p>   
                                                </div>
                                                <div v-else>
                                                    <p class="text-lg">
                                                        <section class="text-xl mt-3">
                                                            {{ error }} 
                                                        </section>
                                                    </p>   
                                                </div>
                                            </label>
                                        </label>
                    <!--end of modal pop up-->
            </div>
                
            </div>
            <!-- Role Desc -->
            <div class="space-y-2 my-4 w-4/6">
                <p class="text-2xl font-medium">
                    Skill Description
                </p>
                <p>
                    {{skill.skillDesc}}
                </p>
            </div>
            <!-- Courses -->
            <div class="space-y-3 my-4">
                <p class="text-2xl font-medium">
                    Courses
                </p>
                <div class="grid grid-cols-2 gap-6 bg-gray-400 rounded-lg my-6 p-8">

                <!-- display course component -->
                <div class="flex" v-for="course of skill.courses">
                    <label for="course-modal" class="btn btn-lg w-11/12" @click="handleCourseClick( course.Course_Name)">
                        <p class="">{{course.Course_ID}}: {{course.Course_Name}}</p>
                        <!-- <p class="">Created on: {{skill.Date_created}}</p> -->
                    </label>
                </div>

                </div>
                    <!-- <div class="grid grid-cols-3 gap-6">
                        <div class="flex justify-evenly" v-for="course of skillCourses"> -->
                            <!-- Course Modal component -->
                            <!-- <label for="course-modal" class="btn modal-button bg-gray-800 rounded-lg w-11/12" @click="handleCourseClick(skillName, course.Course_Name)">
                                {{course.Course_Name}}
                            </label> -->
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
                        <!-- </div>
                    </div>  -->
                <!-- </div> -->
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
import { useSkillStore, useSkillCoursesStore } from '@/store/index.js'
import { getCoursesBySkill, getAllSkills,deleteSkill } from "@/endpoint/endpoint.js";

const router = useRouter()
const route = useRoute()
const skillStore = useSkillStore()
const skillCourseStore = useSkillCoursesStore()

// from params
const skillName = route.params.skillName;

const skill = reactive({
    skillName: '',
    skillID: '',
    skillDesc: '',
    courses: {}
})

const courseModal = reactive({
    courseName: '',
    courseDesc: ''
})

const loading = ref(false)
const error = ref('')
const noErr = ref(true);

;(async() => {
    try {
        // get skill details with chosen skill name
        const skills = await getAllSkills()
        for (var each of skills) {
            if(each.Skill_Name == skillName) {
                skill.skillName = each.Skill_Name
                skill.skillID = each.Skill_ID
                skill.skillDesc = each.Skill_Desc
            }
        }
        
        // get courses with particular skill ID
        const courses = await getCoursesBySkill(skill.skillID)
        for (var course of courses) {
            skill.courses[course.Course_Name] = course
        }
        
        // store role in global store to be use by edit skill page
        skillStore.storeSkill(skill.skillName, skill.skillID, skill.skillDesc, skill.courses)

        // after all API calls made
        loading.value = true
    }
    catch(err) {
        error.value = err
        console.log(err);
    }
})();

function handleEditClick(skillName) {
    router.push({
        name: 'editSkill',
        params: {
            skillName: skillName
        }
    })
}

function handleCourseClick(courseName) {
    courseModal.courseName = courseName
    courseModal.courseDesc = skill.courses[courseName].Course_Desc
}

async function handleDeleteSkill() {
        try {
        const deletedSkill = await deleteSkill(skill.skillID);
        }
        catch (err) {
            error.value = err
            console.log(err);
            noErr.value = false;
        }
    }

</script>

<style scoped>
</style>