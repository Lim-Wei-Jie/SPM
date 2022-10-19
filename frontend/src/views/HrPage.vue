<template>
<!-- eslint-disable -->
    <NavBar/>

    <div class="container mx-auto my-8">
        <p class="text-xl font-bold my-4">
            Current Skills ({{numOfSkills}})
        </p>
        <div class="grid grid-cols-2">

            <!-- Search component -->
            <div class="input-group">
                <!--Search bar-->
                <input type="text" placeholder="Search Skill" class="input input-bordered w-80"/>
                <!-- Search button -->
                <button class="btn btn-square">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                    </svg>
                </button>
            </div>

            <!-- Add new role button -->
            <div class='place-self-end'>
                <button class="btn" @click="handleAddNewSkill">Create New Skill</button>
            </div>

        </div>

        <div class="grid grid-cols-1 gap-6 bg-gray-700 rounded-lg my-6 p-8">

            <!-- Job role component -->
            <div class="flex" v-for="skill in skills">
                <div class="btn btn-lg w-11/12 grid grid-cols-2 " @click="handleSkillClick(skill)">
                    <p class="">{{skill}}</p>
                    <p class="">Created on: {{skill.Date_created}}</p>
                </div>
            </div>

        </div>

    </div>
</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { getAllSkills } from "@/endpoint/endpoint.js";

const router = useRouter()
const skills = ref([])
// const  =  [
//       {
//         "Skill_Desc": "MES Desc", 
//         "Skill_Id": 1234567, 
//         "Skill_Name": "Mechanical Engineeri", 
//         "Date_created": "25 Aug 2022"
//       }, 
//       {
//         "Skill_Desc": "CES Desc", 
//         "Skill_Id": 9741827, 
//         "Skill_Name": "Computer Science Ski", 
//         "Date_created": "20 Aug 2022"
//       }
//     ]

const numOfSkills = ref()

//get all skills
;(async() => {
    await getAllSkills()
    .then((skills) => {
        for (var skill of skills) {
            skills.value.push(skill)
        }
        numOfSkills.value = skills.value.length
    })
    .catch((err) => {
        console.log(err);
    });
})();

function handleSkillClick(skillName) {
    router.push({
        path: `/skill/${skillName}`
    })
}

function handleAddNewSkill() {
    router.push({
        path: '/newSkill'
    })
}
</script>

<style scoped>
</style>