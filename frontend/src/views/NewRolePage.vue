<template>
<!-- eslint-disable -->
<div>
    <NavBar/>
    <div class="container mx-auto my-8">
        <div v-if="loading">

            <!-- Back button -->
            <div>
                <RouterLink to="/manager">
                    <button class="btn btn-circle">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h10a8 8 0 018 8v2M3 10l6 6m-6-6l6-6" />
                        </svg>
                    </button>
                </RouterLink>
            </div>

            <p class="text-3xl my-8"> Add Job Role </p>

            <!-- Form component -->
            <form class="form-control space-y-6" @submit.prevent="handleAddRole">
            
                <!-- Role name input -->
                <div class="space-y-2">
                    <h3 class="font-medium text-lg">Job Role Name</h3>
                    <input type="text" v-model="roleStore.role.roleName" class="input input-bordered w-3/6 text-2xl" placeholder="Job Role Name">
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
import NavBar from '@/components/Navbar.vue'
import { reactive, ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useRoleStore, useAssignSkillsStore } from '@/store/index.js'
import { createRole } from '@/endpoint/endpoint.js'

const router = useRouter()
const route = useRoute()
const roleStore = useRoleStore()
const assignSkillsStore = useAssignSkillsStore()

const loading = ref(true);
const error = ref('');







</script>

<style scoped>
</style>