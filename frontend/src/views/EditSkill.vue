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
                            <RouterLink :to="`/jobRole/${store.role.roleName}`"> {{store.role.roleName}} </RouterLink>
                        </li>
                        <li>
                            Edit role - ({{store.role.roleName}})
                        </li>
                    </ul>
                </div>
    
                <div class="grid grid-cols-2 my-8">
                    <p class="text-3xl"> Edit Job Role </p>
                    <!-- Delete button -->
                    <button @click="handleDeleteRole(store.role.roleID)" class="btn btn-circle place-self-end">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
                        </svg>
                    </button>
                </div>
    
                <!-- Form component -->
                <form class="form-control space-y-6" @submit.prevent="handleEditRole">
    
                    <!-- Role name input -->
                    <div class="space-y-2">
                        <h3 class="font-medium text-lg">Job Role Name</h3>
                        <input type="text" v-model="store.role.roleName" class="input input-bordered w-3/6 text-2xl">
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
                        <p class="font-medium text-lg"> Skills </p>
                        <!-- Skills component -->
                        <div class="grid grid-cols-4 gap-6 bg-gray-700 rounded-lg my-6 p-8">
                            <!-- Skill -->
                            <div class="flex justify-evenly" v-for="(skillDetails, skillName) in store.role.coursesBySkillName" :key="skillName">
                                <div class="text-center bg-gray-800 rounded-lg w-11/12 p-3 relative">
                                    {{ skillName }}
                                    <!-- Remove skill button -->
                                    <label for="remove-modal" class="btn modal-button btn-xs btn-circle btn-error btn-outline absolute right-0 top-0" @click="handleRemoveSkill(skillName)">
                                        <svg class="h-3 w-3" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                                        </svg>
                                    </label>
                                    <!-- Modal pop-up -->
                                    <input type="checkbox" id="remove-modal" class="modal-toggle"/>
                                    <label for="remove-modal" class="modal cursor-default">
                                        <label class="modal-box relative space-y-8">
                                            <p class="text-lg">
                                                Are you sure you want to remove skill:
                                                <section class="text-xl mt-3">
                                                    {{ removeModal.skillName }}
                                                </section>
                                            </p>
                                            <!-- Confirm + cancel buttons -->
                                            <div class="grid grid-cols-2 gap-6">
                                                <div class="flex justify-end">
                                                    <label for="remove-modal" class="btn btn-sm btn-error btn-outline w-3/5" @click="confirmRemoveSkill(removeModal.skillName)">
                                                        Confirm
                                                    </label>
                                                </div>
                                                <div class="flex justify-start">
                                                    <label for="remove-modal" class="btn btn-sm btn-outline w-3/5">
                                                        Cancel
                                                    </label>
                                                </div>
                                            </div>
                                        </label>
                                    </label>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Save button -->
                    <button class="btn w-1/5" type="submit">Save Changes</button>
                    <!-- Cancel button -->
                    <div>
                        <RouterLink :to="`/jobRole/${roleName}`">
                            <div class="btn btn-outline btn-error w-1/5">
                                Cancel
                            </div>
                        </RouterLink>
                    </div>
    
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
    import { useRoleStore } from '@/store/index.js'
    import { getRoleDetails, getSkillsByRole, getCoursesBySkill, deleteRole } from "@/endpoint/endpoint.js";
    
    const router = useRouter()
    const route = useRoute()
    const store = useRoleStore()
    
    // from params
    const roleName = route.params.jobRoleName
    
    const removeModal = reactive({
        skillName: '',
        roleID: store.role.roleID, // for API call
        skillIDArr: [] // for API call
    })
    
    const loading = ref(true);
    const error = ref('');
    
    function handleRemoveSkill(skillName) {
        removeModal.skillName = skillName
    }
    
    function confirmRemoveSkill(skillName) {
        // store Skill ID/s in an array for API call when submit form
        const skillID = store.role.coursesBySkillName[skillName].skillID
        removeModal.skillIDArr.push(skillID.toString())
    
        // removing skill key from coursesBySkillName object in pinia store only
        delete store.role.coursesBySkillName[skillName]
    }
    
    function handleEditRole() {
        // API call here
        
    }
    
    function handleDeleteRole(roleID) {
        console.log(roleID);
    }
    
    </script>
    
    <style scoped>
    </style>