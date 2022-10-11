<template>
<!-- eslint-disable -->
    <div id="app1">
        <NavBar/>
        <!-- Hero Container -->
        <form action="">
            <div class=" hero px-8 py-2">
                <div class="auto-row-max space-y-2">
                    <div id="j-info" class="space-y-2">
                        <h3 class="font-bold text-xl">Job Title</h3>
                        <div id="j-title" class="font-bold grid grid-cols-2">
                            <input type="text" id="job-title" name="job-title" class="text-3xl" placeholder="Software Engineer (Engineering Procurement)" style="width:700px"  v-model="new_job_title">
                            <div class="w-32 place-self-end">
                                <!-- <input type="submit" value="Save Changes" > -->
                                <!--there is something wrong with the styling of button-->
                                <button class="btn bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="button">
                                    Save Changes
                                </button>
                            </div>
                        </div>
                        <div id="j-des" class="space-y-2 w-4/6">
                            
                            <h3 class="font-bold text-xl">Job Description</h3>
                            <input type="text" id="job-des" name="job-des" class="text-xl" placeholder="The Software Engineer / Officer (Engineering Procurement) is responsible for
                            providing administrative support for procurement activities. He/She coordinates
                            with internal teams to gather requirements for procurement, interfaces with
                            vendors for managing delivery schedules, and prepares purchase orders. He
                            maintains documents and reports schedules material purchases and deliveries
                            and performs verification of current inventory.
                            He is comfortable in engaging and interacting with internal and external
                            stakeholders, and is able to multi-task in a fast-paced work environment." style="width:700px"  v-model="new_job_des">
                            
                        </div>  
                    </div>
                    <div id="s-info" class="space-y-3">
            
                        <div id="skills">
                            <h2 class="font-bold text-2xl">Skills</h2>
                            <!--need to add a button for add new skills-->
                            <div class="place-self-end">
                                <button class="bg-sky-500 hover:bg-sky-700 font-bold btn">
                                    Add New Skill
                                </button>
                            </div>
                        </div>

                        <div class="flex flex-col w-full bg-gray-100" v-for="skill in skills">
                            <div>
                                <h4 class="font-bold text-l mx-5 mt-3">Skill Name: </h4>
                                <!--need to insert pop up msg-->
                                <button type="button" class="rounded-md p-2 inline-flex items-end justify-end text-read-400 hover:text-red-500 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500" v-on:click="removeSkill()" v-bind:id="skill">
                                    <span class="sr-only">Remove Skill</span>
                                    <!-- Heroicon name: outline/x -->
                                    <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                                    </svg>
                                </button>
                            </div>
                            <!-- <h2 class="font-medium text-xl mx-5 mt-3">{{skill}}</h2> -->
                            <div class="p-4">
                                <!--need to check with the structure of json data to get the skill des and course des -->
                                <!--need to bind with the particular skill des-->
                                <input type="text"  name="skill" class="text-m  py-2 mx-5 mt-3" v-bind:placeholder="skill.Skill_name" style="width:900px"  v-model="skill.Skill_name" v-bind:id="skill.Skill_name">

                                <h4 class="font-bold text-l mx-5 mt-3">Skill Description: </h4>
                                <div class="p-4">
                                    <!--need to check with the structure of json data to get the skill des and course des -->
                                    <!--need to bind with the particular skill des-->
        
                                    <input type="text" id="skill-des" name="skill-des" class="text-m py-2" v-bind:placeholder="skill.Skill_des" style="width:900px"  v-model="skill.Skill_des" v-bind:id="skill.Skill_des">
                                </div>
                            </div>
                            <div class="w-32">
                            <div class="grid grid-cols-3 gap-4 ml-3 mb-5">
                                <!--Card #1 -->
                                <div class="card w-80 bg-base-100 shadow-xl" v-for="course in skill.Skill_courses">
                                    <div class="card-body">
                                        <div id="top-card" class="flex-row">
                                            <h2 class="card-title mb-2">{{course.course_id}}: {{course.course_name}}</h2>
                                            <h4>{{course.course_desc}}</h4>
                                            <div class="card-actions justify-start">
                                                <button class="btn btn-primary" v-on:click="handleRemoveCourse(course_id)">Remove Course</button>
                                            </div>
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
                <div class='place-self-end'>
                <button class="btn" v-on:click="handleDeleteJob(roleDetailsID)">Delete Job Role</button>
            </div>
            </div>
        </div></div>
        </form>
    </div>

</template>

<script setup>
import NavBar from '../components/NavBar.vue';
import { ref, onBeforeMount } from 'vue'
import { useRouter } from 'vue-router'

const roleDetailsName = ref()
const roleDetailsID = ref()
const roleDetailsDesc = ref()
const course_id = ref()

onBeforeMount(async() => {
    await getRoleDetails(roleName)
    .then((role) => {
        roleDetailsName.value = role.Role_Name
        roleDetailsID.value = role.Role_ID
        roleDetailsDesc.value = role.Role_Desc
    }).catch((err) => {
        console.log(err);
    });
});

function handleRemoveCourse(){

}

function handleDeleteJob() {
    
}


</script>