<template>
<!-- eslint-disable -->
<div>
    <NavBar/>
    <div class="container mx-auto my-8">
        <div v-if="loading">
            <!-- Breadcrumbs component -->
            <div class="text-sm breadcrumbs">
                <ul>
                    <li>
                        <RouterLink to="/login">Home</RouterLink>
                    </li>
                    <li>
                        <RouterLink to="/manager">Job Roles</RouterLink>
                    </li>
                </ul>
            </div>

            <!-- Back button -->
            <div class="my-8">
                <RouterLink to="/login">
                    <button class="btn btn-circle">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h10a8 8 0 018 8v2M3 10l6 6m-6-6l6-6" />
                        </svg>
                    </button>
                </RouterLink>
            </div>

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

                <!-- Add new role button -->
                <div class='place-self-end'>
                    <button class="btn" @click="handleAddNewJob">Add New</button>
                </div>

            </div>

            <div class="grid grid-cols-3 gap-6 bg-gray-700 rounded-lg my-6 p-8">

                <!-- Job role component -->
                <div class="flex justify-evenly " v-for="jobRole in jobRoles">
                    <div class="btn btn-lg w-11/12" @click="handleJobRoleClick(jobRole)">
                        {{jobRole}}
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

</div>

</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
// import Breadcrumb from '@/components/Breadcrumb.vue'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useRoleStore } from '@/store/index.js'
import { getAllRoles } from "@/endpoint/endpoint.js";

const router = useRouter()
const roleStore = useRoleStore()

const jobRoles = ref([])
const numOfJobRoles = ref()
const loading = ref(false);
const error = ref('');

// get all roles
;(async() => {
    try {
        const roles = await getAllRoles()
        for (var role of roles) {
            jobRoles.value.push(role.Role_Name)
        }
        numOfJobRoles.value = jobRoles.value.length

        // after all API calls made
        loading.value = true
    }
    catch(err) {
        error.value = err
        console.log(err);
    }
})();

function handleJobRoleClick(jobRoleName) {
    router.push({
        name: 'jobRole',
        params: {
            jobRoleName: jobRoleName
        }
    })
}

function handleAddNewJob() {
    // reset role store ($reset don't work)
    roleStore.role.roleName = ''
    roleStore.role.roleID = ''
    roleStore.role.roleDesc = ''
    roleStore.role.coursesBySkillName = {}

    router.push({
        name: 'newRole'
    })
}

</script>

<style scoped>
</style>