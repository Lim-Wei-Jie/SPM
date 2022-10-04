<template>
<!-- eslint-disable -->
    <div class="container mx-auto flex items-center h-screen">
        <div class="p-10 grid grid-cols-1 sm:grid-cols-1 md:grid-cols-1 lg:grid-cols-3 xl:grid-cols-3 grow">
            <LoginCard :role="staff" @click="handleLoginStaff"/>
            <LoginCard :role="manager" @click="handleLoginManager"/>
            <LoginCard :role="hr" @click="handleLoginHR"/>
        </div>
    </div>
</template>

<script setup>
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