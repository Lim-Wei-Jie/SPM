<template>
<!-- eslint-disable -->

    <NavBar/>

    <div class="container mx-auto">
        <div class="my-8">
            <p class="text-xl font-bold my-4">
                Current Job Roles ({{numOfJobRoles}})
            </p>
            <div class="grid grid-cols-2">
                <!-- Search component -->
                <div class="input-group">
                    <!--Search bar-->
                    <input type="text" placeholder="Search Job Role" class="input input-bordered w-80"/>
                    <!-- Search button -->
                    <button class="btn btn-square">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                        </svg>
                    </button>
                </div>
                <div class='place-self-end'>
                    <button class="btn" @click="handleAddNewJob">Add New</button>
                </div>
            </div>
        </div>

        <div class="grid grid-cols-3 gap-6 bg-gray-700 rounded-lg my-6 p-8">

            <!-- Job role component -->
            <div class="flex justify-evenly " v-for="jobRole in jobRoles">
                <div class="btn w-64" @click="handleJobRoleClick(jobRole.Role_Name)">
                    {{jobRole.Role_Name}}
                </div>
            </div>

        </div>

    </div>
    
</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { getAllRoles } from "@/endpoint/endpoint.js";

const router = useRouter()

const jobRoles = ref([])
const numOfJobRoles = ref()

onMounted(async() => {
    await getAllRoles()
    .then((data) => {
        for (var each of data) {
            jobRoles.value.push(each)
        }
        numOfJobRoles.value = jobRoles.value.length
    }).catch((err) => {
        console.log(err);
    });
})

function handleJobRoleClick(jobRoleName) {
    router.push({
        path: `/jobRole/${jobRoleName}`
    })
}

</script>

<style scoped>

</style>