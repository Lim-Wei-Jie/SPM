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
            <LearningJourney :ljpsID="LJ.LJ_id" :jobRoleName="LJ.jobRoleName" :completedCourses="LJ.courses.completed" :onGoingCourses="LJ.courses.onGoing" :progress="LJ.progress" :jobRoleID="LJ.jobRoleID"/>
        </div>
    </div>
</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
import Hero from '@/components/Hero.vue'
import { useRouter } from 'vue-router'
import { ref } from 'vue';
import { getLJs, getRoleNameByID } from "@/endpoint/endpoint.js";
import LearningJourney from '../components/LearningJourney.vue';

const router = useRouter()

//check for existing LJ
const staff_ID = '22222222222'
const staff_ID2 = '130003'
const numOfLJ = ref()

//no existing LJ
const title = 'You have no learning journey'
const button = 'Create now'

function searchJobRole() {
    router.push('/staff/searchRole')
}

const LJs = ref([])
;(async() => {
try {
    const res = await getLJs(staff_ID2)
    var LJ_list = []
    for (var LJid in res) {
        //console.log(res[LJid])
        for (var LJ of res[LJid]) {
            LJ_list.push(LJ)
        }
    }
    var ljIdList = []
    for (var LJ of LJ_list) {
        var LJid = LJ[0]
        if (!ljIdList.includes(LJid)) {
            ljIdList.push(LJid)
        }
    }
    var jobNameList = []
    for (var LJ of LJ_list) {
        var jobName = LJ[1]
        if (!jobNameList.includes(jobName)) {
            jobNameList.push(jobName)
        }
    }

    for (let i = 0; i < ljIdList.length; i++) {
        //get role name
        const Role_Name = await getRoleNameByID(jobNameList[i])

        //get all courses and status
        var oneCourseList = []
        for (var LJ of LJ_list) {
            if (LJ[0] == ljIdList[i]) {
                oneCourseList.push([LJ[2], LJ[3]])
            }
        }

        var completedCourseList = []
        var onGoingCourseList = []
        for (var x in oneCourseList) {
            if (oneCourseList[x][1] == 'Completed') {
                completedCourseList.push(oneCourseList[x][0])
            } else {
                onGoingCourseList.push(oneCourseList[x][0])
            }
        }
        var completedNo = completedCourseList.length
        var totalNo = oneCourseList.length
        var completedPer = Math.ceil((completedNo/totalNo) * 100)
        
        LJs.value.push(
            {
                LJ_id: ljIdList[i],
                jobRoleName: Role_Name,
                jobRoleID: jobNameList[i],
                courses: {
                    completed: completedCourseList,
                    onGoing: onGoingCourseList
                },
                progress: completedPer
            }
        ) 
    }
}
catch(err){
    console.log(err)
    numOfLJ.value = 0
}
})();


</script>

<style scoped>

</style>