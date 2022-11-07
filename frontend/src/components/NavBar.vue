<template>
    <div class="navbar bg-base-100">
        <div class="navbar-center">
            <btn class="btn btn-ghost normal-case text-xl" @click="home()">LJPS</btn>
        </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
function home() {
    router.push({
        path: `/`
    })
}
</script>

<style scoped>

</style>