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
        
        <div v-for="LJ in LJs">
            <LearningJourney :jobRoleName="LJ.jobRoleName" :completedCourses="LJ.courses.completed" :onGoingCourses="LJ.courses.onGoing" :progress="LJ.progress"/>
        </div>
    </div>
</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
import Hero from '@/components/Hero.vue'
import LearningJourney from '@/components/LearningJourney.vue'
import { useRouter } from 'vue-router'
import { ref } from 'vue';
import { getRegistration } from "@/endpoint/endpoint.js";

const router = useRouter()

//check for existing LJ
const staff_ID = '140002'
const numOfLJ = ref()
var LJs = ref([])

//no existing LJ
const title = 'You have no learning journey'
const button = 'Create now'

function searchJobRole() {
    router.push('/staff/searchRole')
}


;(async() => {
    await getRegistration(staff_ID)
    .then((response) => {
        var jobRole= "Job Role Name"
        var completedCourses = []
        var onGoingCourses = []
        for (var registration of response) {
            if (registration.completion_status == "Completed"){
                completedCourses.push(registration.course_id)
            } else {
                onGoingCourses.push(registration.course_id)
            }
        }
        
        //calculation of progress
        var totalCourses = completedCourses.length + onGoingCourses.length
        var progress = Math.ceil((completedCourses.length / totalCourses) * 100)

        //add data to overall Learning Journeys
        LJs.value.push(
            {
                jobRoleName: jobRole,
                courses: {
                    completed: completedCourses,
                    onGoing: onGoingCourses
                },
                progress: progress
            }
        ) 
        
        //NEED TO BE UPDATED
        numOfLJ.value = response.length
    }).catch((err) => {
        console.log(err);
        numOfLJ.value = 0
    });
})();


/*
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
*/

</script>

<style scoped>

</style>