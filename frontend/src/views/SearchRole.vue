<template>
<!-- eslint-disable -->
    <NavBar/>
    <div class="container mx-auto my-8">
        <div class="form-control w-full">
            <div class="input-group w-full">
                <input type="text" class="input input-bordered w-full" placeholder="Search Job Title.." v-model="searchQuery" @keydown="filterResults"/>
                <button class="btn btn-square">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
                </button>
            </div>
            
            <div v-if="searchQuery != ''" class="w-full">
                <ul v-for="jobRole in filteredJobs" class="w-full">
                    <li class="bg-slate-50 hover:shadow-lg hover:bg-slate-100 px-5 py-3 " @click="createLJ(jobRole)" value="">
                        {{jobRole}}
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import { getAllRoles } from "@/endpoint/endpoint.js";


const router = useRouter()
function createLJ(jobRoleName) {
    router.push({
        path: `/staff/create/${jobRoleName}`
    })
}

const selectedJobRole = 'Mechanical Engineeri'

const jobRoles = ref()
const searchQuery = ref()



// get all roles
;(async() => {
    await getAllRoles()
    .then((roles) => {
        var jobRoleArray = []
        for (var role of roles) {
            jobRoleArray.push(role.Role_Name)
        }
        jobRoles.value = jobRoleArray
    })
    .catch((err) => {
        console.log(err);
    });
})();


//METHOD 1

const filteredJobs = ref()
function filterResults() {
    filteredJobs.value = jobRoles.value.filter(jobRole => jobRole.toLowerCase().indexOf(searchQuery.value.toLowerCase()) > -1);
}


</script>

<style scoped>

</style>