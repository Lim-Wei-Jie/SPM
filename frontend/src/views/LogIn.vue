<template>
<!-- eslint-disable -->
<div>
    <NavBar/>
    <div class="container mx-auto my-8">
        <div class="flex items-center">
            <!-- Back button -->
            <div>
                <RouterLink to="/">
                    <button class="btn btn-circle">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h10a8 8 0 018 8v2M3 10l6 6m-6-6l6-6" />
                        </svg>
                    </button>
                </RouterLink>
            </div>
            <!-- Card component -->
            <div class="p-10 grid grid-cols-1 sm:grid-cols-1 md:grid-cols-1 lg:grid-cols-3 xl:grid-cols-3 grow">
                <LoginCard :role="staff" @click="handleLoginStaff"/>
                <LoginCard :role="manager" @click="handleLoginManager"/>
                <LoginCard :role="hr" @click="handleLoginHR"/>
            </div>
        </div>
    </div>
</div>

</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
import LoginCard from '@/components/LoginCard.vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const staff = 'Staff'
const manager = 'Manager'
const hr = 'Human Resource'

function handleLoginStaff() {
    router.push('/staff')
}

function handleLoginManager() {
    router.push('/manager')
}

function handleLoginHR() {
    router.push('/hr')
}

</script>

<style scoped>

</style>