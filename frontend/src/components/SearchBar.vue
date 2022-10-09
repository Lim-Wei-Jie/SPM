<template>
    <div class="form-control">
        <div class="input-group">
            <input type="text" class="input input-bordered" :placeholder="placeholder" :value="modelValue" @load="$emit('update:placeholderValue', $event.target.value)" @input="$emit('update:modelValue', $event.target.value)" />
            <button class="btn btn-square">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
            </button>
        </div>
    </div>
</template>

<script setup>

const props = defineProps({
    placeholder: {
        type: String,
        default: ''
    },
})

const emit = defineEmits(['update:modelValue'])
        
</script>