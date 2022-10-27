<template>
<!-- eslint-disable -->
    <NavBar/>

    <div class="container mx-auto my-8">
        <div v-if="loading">
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

            <!-- Add new skill button -->
            <div class='place-self-end'>
                <button class="btn" @click="handleAddNewSkill">Create New Skill</button>
            </div>

        </div>

        <div class="grid grid-cols-1 gap-6 bg-gray-400 rounded-lg my-6 p-8">

            <!-- display skill component -->
            <div class="flex" v-for="skill in allSkills">
                <div class="btn btn-lg w-11/12" @click="handleSkillClick(skill)">
                    <p class="">{{skill}}</p>
                    <!-- <p class="">Created on: {{skill.Date_created}}</p> -->
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
</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { getAllSkills } from "@/endpoint/endpoint.js";

const router = useRouter()
const allSkills = ref([])
const numOfSkills = ref()
const loading = ref(false);
const error = ref('');

// //get all skills

;(async() => {
    try {
        const skills = await getAllSkills()
        for (var skill of skills) {
            allSkills.value.push(skill.Skill_name)
        }
        allSkills.value.sort();
        numOfSkills.value = allSkills.value.length

        // after all API calls made
        loading.value = true
    }
    catch(err) {
        error.value = err
        console.log(err);
    }
})();

function handleSkillClick(skill) {
    router.push({
        name: 'skill',
        params: {
            skillName: skill
        }
    })
}

function handleAddNewSkill() {
    router.push({
        name: 'newSkill'
    })
}
</script>

<style scoped>
</style>