<template>
    <div class="hero min-h-screen bg-base-200">
        <div class="hero-content text-center">
            <div class="max-w-md">
                <p class="py-6">{{title}}</p>
                <button class="btn modal-button">{{button}}</button>
            </div>
        </div>
    </div>
</template>

<script setup>

const props = defineProps({
    title: {
        type: String,
        default: ''
    },
    button: {
        type: String,
        default: ''
    }
});
    
</script>