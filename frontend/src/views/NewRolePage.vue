<template>
    <!-- eslint-disable -->
   
    <div id="app1">
        <NavBar/>

        <!-- Hero Container -->
        <!-- <form> -->
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
                                </fieldset> 
                            </div>           
                               
                    </div>
                </div>
                <div class="w-32 place-self-center">
                    <label class="btn" for="my-modal" v-on:click="display()">Create Job Role</label>
                </div>
                <!-- modal pop up for errors-->
                <div v-if="hasErros">
                    <label class="btn" for="my-modal">Erros</label>
                    <input type="checkbox" id="my-modal" class="modal-toggle" />
                            <div class="modal">
                                <div class="modal-box">
                                    <div class="modal-action">
                                        <h4>Errors:</h4>
                                        <ol>
                                            <li v-for="error in errors">Please {{error}}</li> 
                                        </ol>
                                    <label for="my-modal" class="btn btn-outline btn-error" >Ok</label>
                                    </div>
                                </div>
                            </div>
                </div>

                <!-- modal pop up to create job role-->
                <div v-else>
                    <input type="checkbox" id="my-modal" class="modal-toggle" />
                            <div class="modal">
                                <div class="modal-box">
                                    <div class="modal-action">
                                        <h4>You are creating {{new_job_title}}.</h4>
                                    <label for="my-modal" class="btn btn-outline btn-error" @click="createRole(newJobRoleData); mapSkillsToJob(skillstoJobRoleData)" >Create Job Role</label>
                                    </div>
                                </div>
                            </div>
                </div>
                <div v-if="hasJobError">
                    <input type="checkbox" id="my-modal" class="modal-toggle" />
                            <div class="modal">
                                <div class="modal-box">
                                    <div class="modal-action">
                                        <h4>{{jobError}}</h4>
                                    <label for="my-modal" class="btn btn-outline btn-error">Ok</label>
                                    </div>
                                </div>
                            </div>
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
import { mapSkillsToJob } from "@/endpoint/endpoint.js";

const new_job_title = ref();
const new_job_des = ref();
const newJobRoleData = ref([]);
const selectedSkill = ref([]);
const numOfSkills = ref();
const hasErros = ref(false);
const errors = ref([]);
const skillstoJobRoleData = ref();
const hasJobError = ref(false);
const jobError = ref();
const skills = ref([]);



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
    // console.log(new_job_title.value);
    if(new_job_title.value == null){
        errors.value.push('enter a job title');
        hasErros.value = true;
    }
    if(new_job_des.value == null){
        errors.value.push('enter job description');
        hasErros.value = true;
    }
    if(selectedSkill.value.length == 0){
        errors.value.push('select at least 1 skill');
        hasErros.value = true;
    }
    //console.log(selectedSkill);
    // this.newJobRoleData.push(this.new_job_title, this.new_job_des, this.selectedSkill);
    newJobRoleData.value.push(new_job_title.value, new_job_des.value);
    //console.log(this.newJobRoleData);
    skillstoJobRoleData.value.push()
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

// error from creating job role
;(async() => {
    await createRole(newJobRoleData)
    .catch((err) => {
        hasJobError.value = true;
        jobError.value = err.message;
        //"Role already exists."
        //"An error occurred creating the Role."
        console.log(err.message);
    });
})();

//error from skill mapping to job role 
;(async() => {
    await mapSkillsToJob(skillstoJobRoleData)
    .catch((err) => {
        // hasJobError.value = true;
        // jobError.value = err.message;
        //"Role already exists."
        //"An error occurred creating the Role."
        console.log(err.message);
    });
})();




</script>

<style scoped>

</style>