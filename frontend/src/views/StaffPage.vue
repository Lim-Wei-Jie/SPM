<template>
<!-- eslint-disable -->
    <NavBar/>
    <Hero v-if="numOfLJ == 0" :title="title" :button="button" @click="searchJobRole"/>
    <div v-else class="container mx-auto my-8">
        <div class="flex justify-between">
            <p class="text-2xl font-bold">
                Learning Journey Progress
            </p>
            <button class="btn" @click="searchJobRole">Add New</button>
        </div>
        
        <div v-for="LJ in learningJourneys">
            <LearningJourney :jobRoleName="LJ.jobRoleName" :completedCourses="LJ.courses.completed" :inProgCourses="LJ.courses.inProgress"/>
        </div>
    </div>
</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
import Hero from '@/components/Hero.vue'
import LearningJourney from '@/components/LearningJourney.vue'
import { useRouter } from 'vue-router'
import { ref } from 'vue';

const router = useRouter()

//check for existing LJ
const numOfLJ = ref(3)

//no existing LJ
const title = 'You have no learning journey'
const button = 'Create now'

function searchJobRole() {
    router.push('/staff/searchRole')
}

//fake data
const learningJourneys = ref({
    learningJourney1: {
        jobRoleName: "Mechanical Engineeri",
        courses: {
            completed: ["Course4", "Course5"],
            inProgress: ["Course1", "Course2", "Course3"]
        }
    },
    learningJourney2: {
        jobRoleName: "Computer Science",
        courses: {
            completed: ["Course9", "Course10"],
            inProgress: ["Course6", "Course7", "Course8"]
        }
    }
})

</script>

<style scoped>

</style>