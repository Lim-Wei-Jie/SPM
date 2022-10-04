<template>
<!-- eslint-disable -->
    <div class="container mx-auto flex items-center h-screen">
        <div class="p-10 grid grid-cols-1 sm:grid-cols-1 md:grid-cols-1 lg:grid-cols-3 xl:grid-cols-3 grow">
            <LoginCard :role="staff" />
            <LoginCard :role="manager" />
            <LoginCard :role="hr" />
        </div>
    </div>
</template>

<script setup>
import LoginCard from '@/components/LoginCard.vue'

const staff = 'Staff'
const manager = 'Manager'
const hr = 'Human Resource'

</script>

<style scoped>

</style>