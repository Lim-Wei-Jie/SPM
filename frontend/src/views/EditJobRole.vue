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
                        <RouterLink to="/manager">Job Role</RouterLink>
                    </li> 
                    <li>
                        <RouterLink :to="`/jobRole/${roleName}`"> {{roleName}} </RouterLink>
                    </li>
                    <li>
                        Edit role - ({{roleName}})
                    </li>
                </ul>
            </div>

            <div class="grid grid-cols-2 my-8">
                <p class="text-3xl"> Edit Job Role </p>
                <!-- Delete button -->
                <button @click="handleDeleteClick(store.role.roleID)" class="btn btn-circle place-self-end">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                    </svg>
                </button>
            </div>

            <!-- Form component -->
            <form class="form-control space-y-6" @submit.prevent="onSubmit">
                <!-- {{store.role.roleName}}
                {{store.role.roleID}}
                {{store.role.roleDesc}}
                {{store.role.coursesBySkillName}} -->
                
                <!-- Role name input -->
                <div class="space-y-2">
                    <h3 class="font-medium text-lg">Job Role Name</h3>
                    <input type="text" v-model="roleName" class="input input-bordered w-3/6 text-2xl">
                </div>
                
                <!-- Role desc input -->
                <div class="space-y-2 w-4/6">
                    <p class="font-medium text-lg">
                        Job Role Description
                    </p>
                    <input type="text" v-model="store.role.roleDesc" class="input input-bordered w-full">
                </div>

                <!-- Role skills -->
                <div class="space-y-3">
                    <p class="font-medium text-lg">
                        Skills
                    </p>
                    <!-- Skills component -->
                    <div class="grid grid-cols-4 gap-6 bg-gray-700 rounded-lg my-6 p-8">
                        <!-- Skill -->
                        <div class="flex justify-evenly" v-for="(courseArr, skill) in store.role.coursesBySkillName" :key="skill">
                            <div class="btn noHover bg-gray-800 rounded-lg w-11/12">
                                {{skill}}
                            </div>
                        </div>
                    </div>
                </div>

                <button class="btn w-1/5" type="submit">Save Changes</button>
                
            </form>
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
import NavBar from '../components/NavBar.vue';
import { reactive, ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useRoleStore } from '@/store/role.js'
import { getRoleDetails, getSkillsByRole, getCoursesBySkill, deleteRole } from "@/endpoint/endpoint.js";

const router = useRouter()
const route = useRoute()
const store = useRoleStore()

// from params
const roleName = route.params.jobRoleName

const loading = ref(true);
const error = ref('');

function onSubmit() {
    console.log('submitted');
}

function handleDeleteClick(roleID) {
    console.log(roleID);
}

</script>

<style scoped>
.noHover{
    pointer-events: none;
}

</style>