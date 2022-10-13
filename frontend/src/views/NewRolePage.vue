<template>
    <!-- eslint-disable -->
   
    <div id="app1">
        <NavBar/>

        <!-- Hero Container -->
        <!-- <form action=""> -->
            <div class="container mx-auto my-8">
                <div class="auto-row-max space-y-2">
                    <div id="j-info" class="space-y-2">
                        <h1 class="font-bold text-2xl">Creating Job Role</h1>
                        <h3 class="font-bold text-xl">Job Title</h3>
                        <div id="j-title" class="grid grid-cols-2">
                            <input type="text" id="job-title" name="job-title" class="text-xl bg-gray-100 py-2 " placeholder="Enter Name of Job Role" style="width:700px"  v-model="new_job_title">
                            
                        </div>
                        <div id="j-des" class="space-y-2 w-4/6">
                            
                            <h3 class="font-bold text-xl">Job Description</h3>
                                <input type="text" id="job-des" name="job-des" class="text-xl  bg-gray-100 py-2" placeholder="Enter Job Description here..." style="width:700px; height:200px;" v-model="new_job_des" >
                           
                        </div>  
                    </div>
                    <div id="s-info" class="space-y-3">
            
                        <div id="skills">
                            <h2 class="font-bold text-2xl">Skills {{numOfSkills}}</h2>
                            <!--need to add a button for add new skills-->
                            <!-- <div class="place-self-end">
                                <button class="bg-sky-500 hover:bg-sky-700 font-bold btn">
                                    Add New Skill
                                </button>
                            </div> -->
                        </div>

                        <div class="bg-gray-100 pt-2 pb-2">
                            
                        <div class="grid grid-cols-3 gap-4 ml-3 mb-5 mt-2" v-for="skill in skills">
                            <div class="card w-80 bg-base-100 shadow-xl">
                                <fieldset>      
                                    <!-- <legend>What is Your Favorite Pet?</legend>       -->
                                    <input type="checkbox" v-bind:value="skill.Skill_name" v-bind:id="skill.Skill_id" v-model="selectedSkill" class="m-3">{{skill.Skill_name}} <br>    
                                    <!-- <input type="submit" value="Submit now" />       -->
                                </fieldset> 
                            </div>           
                                <!--Card #1 -->
                                <!-- <div class="card w-80 bg-base-100 shadow-xl">
                                    <div class="card-body hover:bg-red-300" v-on:click="getCourses()" >
                                        <div id="top-card" class="flex-row">  
                                            <h2 class="card-title mb-2">{{skill.Skill_name}}</h2>
                                            <p>{{skill.Skill_desc}}</p> 
                                        </div>
                                    </div>
                                </div> -->


                                   
                           
                            <!-- courses will be displayed when a skill is selected-->
                            <!-- <div class="w-32" v-if="selectedSkill">
                            <div class="grid grid-cols-3 gap-4 ml-3 mb-5"> -->
                                <!--Card #1 -->
                                <!-- <div class="card w-80 bg-base-100 shadow-xl" v-for="course in skill.Skill_courses">
                                    <div class="card-body">
                                        <div id="top-card" class="flex-row">
                                            <h2 class="card-title mb-2">{{course.course_id}}: {{course.Course_Name}}</h2>
                                            <h4>{{course.Course_Desc}}</h4>
                                            
                                        </div> -->
                                        <!-- <p>If a dog chews shoes whose shoes does he choose?</p> -->
                                        <!-- <div class="card-actions justify-end">
                                            <button class="btn btn-primary">Buy Now</button>
                                        </div> -->
                                    <!-- </div>
                                </div>    -->
                        <!-- </div>
                        </div> -->
                    </div>
                </div>
                <div class="w-32 place-self-center">
                    <!--need to have v-on to delete job role from database-->
                    <!-- v-on:click="createRole(newJobRoleData)" -->
                    <button class="btn"  v-on:click="display()">Create Job Role</button>
                </div>
            </div>
            </div>
            </div>
        <!-- </form> -->
    </div>
</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
import { ref, toRefs, onBeforeMount } from 'vue'
import { createRole } from '@/endpoint/endpoint.js'
import { getAllSkills } from "@/endpoint/endpoint.js";

const new_job_title = ref();
const new_job_des = ref();
const newJobRoleData = ref([]);
const selectedSkill = ref([]);
const numOfSkills = ref();

// const skills = ref([
//       {
//         "Skill_desc": "MES Desc", 
//         "Skill_id": 1234567, 
//         "Skill_name": "Mechanical Engineeri", 
//         "Skill_status": null
//       }, 
//       {
//         "Skill_desc": "CES Desc", 
//         "Skill_id": 9741827, 
//         "Skill_name": "Computer Science Ski", 
//         "Skill_status": null
//       }
//     ]);

function display(){
   
    this.newJobRoleData.push(this.new_job_title, this.new_job_des, this.selectedSkill);
    console.log(this.newJobRoleData);
}

// get all skills
;(async() => {
    await getAllSkills()
    .then((skills) => {
        for (var skill of skills) {
            skills.value.push(skill.skill_Name)
        }
        numOfSkills.value = skills.value.length
    })
    .catch((err) => {
        console.log(err);
    });
})();



</script>

<style scoped>

</style>