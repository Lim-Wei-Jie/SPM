<template>
    <!-- eslint-disable -->
   
    <div id="app1">
        <NavBar/>

        <!-- Hero Container -->
        <form action="">
            <div class=" hero px-8 py-2">
                <div class="auto-row-max space-y-2">
                    <div id="j-info" class="space-y-2">
                        <h1 class="font-bold text-2xl">Creating Job Role</h1>
                        <h3 class="font-bold text-xl">Job Title</h3>
                        <div id="j-title" class="grid grid-cols-2">
                            <input type="text" id="job-title" name="job-title" class="text-xl bg-gray-100 py-2 " placeholder="Enter Name of Job Role" style="width:700px"  v-model="new_job_title">
                            
                        </div>
                        <div id="j-des" class="space-y-2 w-4/6">
                            
                            <h3 class="font-bold text-xl">Job Description</h3>
                                <input type="text" id="job-des" name="job-des" class="text-xl bg-gray-100 py-2" placeholder="Enter Job Description here..." style="width:700px"  v-model="new_job_des">
                           
                        </div>  
                    </div>
                    <div id="s-info" class="space-y-3">
            
                        <div id="skills">
                            <h2 class="font-bold text-2xl">Skills</h2>
                            <!--need to add a button for add new skills-->
                            <!-- <div class="place-self-end">
                                <button class="bg-sky-500 hover:bg-sky-700 font-bold btn">
                                    Add New Skill
                                </button>
                            </div> -->
                        </div>

                        <div class="bg-gray-100">
                            
                            <div v-for="skill in skills">
                            <div class="p-4">
                                <label for="cars" class="font-bold text-l mx-5 mt-3">Skill Name:</label>

                                <select class="py-2" v-model="selected" style="width:600px" v-on:change="onChange($event)">
                                    <option v-bind:value="skill.Skill_name">
                                        {{skill.Skill_name}}
                                    </option>
                                </select>

                                <!--need to insert pop up msg-->
                                <div class="place-items-end">
                                    <button type="button" class="rounded-md p-2 inline-flex items-end justify-end text-read-400 hover:text-red-500 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500" v-on:click="removeSkill()" v-bind:id="skill">
                                        <span class="sr-only">Remove Skill</span>
                                        <!-- Heroicon name: outline/x -->
                                        <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                                        </svg>
                                    </button>
                                </div>
                            </div>
                            <!-- <h2 class="font-medium text-xl mx-5 mt-3">{{skill}}</h2> -->
                            <div class="p-4">
                                <!--need to check with the structure of json data to get the skill des and course des -->
                                <!--need to bind with the particular skill des-->


                                <h4 class="font-bold text-l mx-5 mt-3">Skill Description: </h4>
                                <div class="p-4">
                                    <!--need to check with the structure of json data to get the skill des and course des -->
                                    <!--need to bind with the particular skill des-->
                                    
                                    <input type="text" id="skill-des" name="skill-des" class="text-m py-2" placeholder="Enter Skill Description here..." style="width:900px"  v-model="skill.Skill_des" v-bind:id="skill.Skill_des">
                                </div>
                            </div>

                            <!-- courses will be displayed when a skill is selected-->
                            <div class="w-32" v-if="selectedSkill">
                            <div class="grid grid-cols-3 gap-4 ml-3 mb-5">
                                <!--Card #1 -->
                                <div class="card w-80 bg-base-100 shadow-xl" v-for="course in skill.Skill_courses">
                                    <div class="card-body">
                                        <div id="top-card" class="flex-row">
                                            <h2 class="card-title mb-2">{{course.course_id}}: {{course.Course_Name}}</h2>
                                            <h4>{{course.Course_Desc}}</h4>
                                            
                                        </div>
                                        <!-- <p>If a dog chews shoes whose shoes does he choose?</p> -->
                                        <!-- <div class="card-actions justify-end">
                                            <button class="btn btn-primary">Buy Now</button>
                                        </div> -->
                                    </div>
                                </div>   
                        </div>
                        </div>
                    </div>
                </div>
                <div class="w-32 place-self-center">
                    <!--need to have v-on to delete job role from database-->
                    <button class="btn" v-on:click="handleNewJobRole()">Create Job Role</button>
                </div>
            </div>
            </div>
            </div>
        </form>
    </div>
</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
import { ref, toRefs, onBeforeMount } from 'vue'

const selected = ref()
const selectedSkill = false;
const targetSkillID = ref();

function onChange(event){
    selectedSkill = true;
    targetSkillID = event.target.value; 
    //need to call axios to fetch the courses related to the skill id 
}

function handleNewJobRole() {
    router.push({
        path: '/manager'
    })
}
</script>

<style scoped>

</style>