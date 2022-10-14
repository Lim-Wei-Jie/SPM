<template>
    <div class="bg-slate-100 rounded-md px-10 py-7 my-4">
        <div class="grid grid-cols-2">
            <p class="text-xl font-bold underline underline-offset-8">
                {{jobRoleName}}
            </p>
            <button @click="handleEditClick(jobRoleName)" class="btn btn-circle place-self-end">
                <svg class="w-4 h-4 fill-current" viewBox="0 0 20 20"><path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z"></path></svg>
            </button>
        </div>
        <!-- In Progress Section-->
        <div v-show="inProgCourses != []" class="inProg">
            <p class="text-lg font-normal">
                In Progress
            </p>
            <div class="grid grid-cols-3 gap-4 my-4">
                <div v-for="course in inProgCourses" class="bg-slate-50 rounded-md px-2 py-2 outline outline-1 outline-slate-400">
                    {{ course }}
                </div>
            </div>
        </div>
        
        <!-- Completed Section-->
        <div v-show="completedCourses != []" class="completed">
            <p class="text-lg font-normal ">
                Completed
            </p>

            <div class="grid grid-cols-3 gap-4 my-4">
                <div v-for="course in completedCourses" class="bg-slate-50 rounded-md px-2 py-2 outline outline-1 outline-slate-400">
                    {{ course }}
                </div>
            </div>
        </div>

        <!-- Progress Bar -->
        <div class="flex flex-row items-center w-full gap-4">
            <progress class="progress w-full" value="40" max="100"></progress>
            <p>40%</p>
        </div>
        
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const props = defineProps({
    jobRoleName: {
        type: String,
        default: ''
    },
    completedCourses: {
        type: Array,
        default: []
    },
    inProgCourses: {
        type: Array,
        default: []
    }
});


const router = useRouter()
function handleEditClick(jobRoleName) {
    router.push({
        path: `staff/edit/${jobRoleName}`
    })
}


</script>