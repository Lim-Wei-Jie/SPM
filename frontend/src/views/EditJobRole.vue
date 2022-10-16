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
                            <input type="text" v-bind:id="roleDetailsID" name="job-title" class="text-3xl"  style="width:700px"  v-model="roleDetailsName">
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
                        <!-- Skills -->
                        <div class="space-y-3 my-4">
                            <p class="text-2xl font-medium">
                                Skills
                            </p>
                            <!-- Skills component -->
                            <div class="bg-gray-700 rounded-lg my-6 p-8" v-for="(courseArr, skill) in coursesBySkillName" :key="skill">
                                <!-- Skill -->
                                <div class="font-medium text-lg mb-5">
                                    {{skill}}
                                    <!--remove skill -->
                                    <label for="my-modal" class="btn rounded-md p-2 inline-flex items-end justify-end text-read-400 hover:text-red-500 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500" v-on:click="removeSkill()" v-bind:id="skillID">
                                        <span class="sr-only">Remove Skill</span>
                                        <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                                        </svg>
                                    </label>

                                    <!-- modal pop up to delete skill-->
                                    <!-- <div v-if="hasRemoveSkill">
                                        <input type="checkbox" id="my-modal" class="modal-toggle" />
                                                <div class="modal">
                                                    <div class="modal-box">
                                                        <div class="modal-action">
                                                            <h4>You are deleting {{skillName}}.</h4>
                                                        <label for="my-modal" class="btn btn-outline btn-error" @click="deleteSkill(skillID)" >Delete Skill</label>
                                                        </div>
                                                    </div>
                                                </div>
                                    </div> -->
                                    <!--end of remove skill-->
                                </div>
                                <!-- Courses -->
                                <div class="grid grid-cols-3 gap-6">
                                    <div class="flex justify-evenly" v-for="course of courseArr">
                                        <div class="btn bg-gray-800 rounded-lg w-11/12">
                                            {{course}}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!--to be commented out-->
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
                                    </div>
                                </div>   
                            

                        </div>
                    </div>
                </div>
                 <!--end of to be commented out-->

                <div class='place-self-end'>
                <label class="btn" for="my-modal" v-on:click="display()">Delete Job Role</label>
                <!-- modal pop up to delete job role-->
                <div v-if="removeJob">
                    <input type="checkbox" id="my-modal" class="modal-toggle" />
                            <div class="modal">
                                <div class="modal-box">
                                    <div class="modal-action">
                                        <h4>You are deleting {{roleDetailsName}}.</h4>
                                    <label for="my-modal" class="btn btn-outline btn-error" @click="deleteJob(roleDetailsID)" >Delete Job Role</label>
                                    </div>
                                </div>
                            </div>
                </div>
                <!-- modal pop up when there is error in delete job role-->
                <div v-if="hasDeleteError">
                    <input type="checkbox" id="my-modal" class="modal-toggle" />
                            <div class="modal">
                                <div class="modal-box">
                                    <div class="modal-action">
                                        <h4>{{deleteError}}</h4>
                                    <label for="my-modal" class="btn btn-outline btn-error">Ok</label>
                                    </div>
                                </div>
                            </div>
                </div>
               
            </div>
            </div>
        </div></div>
        </form>
    </div>

</template>

<script setup>
import NavBar from '../components/NavBar.vue';
import { ref, toRefs,onBeforeMount } from 'vue'
import { useRouter } from 'vue-router'
import { getRoleDetails, getSkillsByRole, getCoursesBySkill, deleteRole } from "@/endpoint/endpoint.js";

const router = useRouter()

const props = defineProps({
    jobRoleName: {
        type: String
    }
});
// props to be use in script setup, break down proxy
const { jobRoleName } = toRefs(props)
const roleName = JSON.parse(JSON.stringify(jobRoleName))._object.jobRoleName

// can try reactive()
const roleDetailsName = ref()
const roleDetailsID = ref()
const roleDetailsDesc = ref()
const skillNames = ref([])
const coursesBySkillName = ref({}) // key=skillName, value=courseName
const removeJob = ref(false);
const deleteError = ref();
const hasDeleteError = ref(false);


;(async() => {
    await Promise.all([
        // get role name, ID, and description
        getRoleDetails(roleName)
        .then((role) => {
            roleDetailsName.value = role.Role_Name
            roleDetailsID.value = role.Role_ID
            roleDetailsDesc.value = role.Role_Desc

            // get skills with role ID
            getSkillsByRole(roleDetailsID.value)
            .then((data) => {
                for (var each of data) {
                    skillNames.value.push(each.Skill_name)

                    // get courses with skill IDs
                    const skillID = each.Skill_id
                    const skillName = each.Skill_name

                    getCoursesBySkill(skillID)
                    .then((data) => {
                        for (var each of data) {
                            // check if skillName exist in object
                            if (coursesBySkillName.value[skillName]) {
                                coursesBySkillName.value[skillName].push(each.Course_Name)
                            } else {
                                coursesBySkillName.value[skillName] = [each.Course_Name]
                            }
                        }
                    })
                    .catch((err) => {
                        console.log(err);
                    })
                }

            })
            .catch((err) => {
                console.log(err);
            })

        })
        .catch((err) => {
            console.log(err);
        }),
        
    ]);
})();

function handleRemoveCourse(){

}

function display() {
    removeJob.value = true;
}

// error from deleting job role
;(async() => {
    await deleteRole(roleDetailsID)
    .catch((err) => {
        hasDeleteError.value = true;
        deleteError.value = err.message;
        //"Role already exists."
        //"An error occurred creating the Role."
        console.log(err.message);
    });
})();

</script>