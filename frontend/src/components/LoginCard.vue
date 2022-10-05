<template>
<!-- eslint-disable -->
    <div class="flex justify-evenly">
        <!-- Role card component -->
        <div class="card card-normal card-bordered w-10/12 h-96 shadow-2xl btn">
            <!-- placeholder avatar -->
            <!-- <figure class="px-10 pt-10">
                <div class="avatar">
                    <div class="avatar w-24 rounded">
                        <img src="https://placeimg.com/192/192/people" />
                    </div>
                </div>
            </figure> -->
            <!-- Text -->
            <div class="card-body items-center text-center">
                <h2 class="card-title">{{role}}</h2>
            </div>
        </div>
    </div>

</template>

<script setup>

const props = defineProps({
    role: {
        type: String,
        default: ''
    }
});

</script>

<style scoped>

</style>