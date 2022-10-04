<template>
<!-- eslint-disable -->

    <!-- Hero Container -->
    <div class="hero min-h-screen bg-base-200">
        <div class="hero-content text-center">
            <div class="max-w-md">
                <h1 class="text-5xl font-bold">Hello there</h1>
                <p class="py-6">Provident cupiditate voluptatem et in. Quaerat fugiat ut assumenda excepturi exercitationem quasi. In deleniti eaque aut repudiandae et a id nisi.</p>
                <!-- <label for="my-modal-4" class="btn modal-button">LOG IN</label> -->
                <button @click="handleClickLogIn" class="btn btn-xs sm:btn-sm md:btn-md lg:btn-lg">LOG IN</button>
            </div>
        </div>
    </div>

    <!-- Log In Modal -->
    <!-- <input type="checkbox" id="my-modal-4" class="modal-toggle" />
    <label for="my-modal-4" class="modal cursor-pointer">
        <label class="modal-box relative" for="">
            <h3 class="text-lg font-bold">Log In</h3>
        </label>
    </label> -->

</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

function handleClickLogIn() {
    router.push('/login' )
}

</script>

<style scoped>

</style>