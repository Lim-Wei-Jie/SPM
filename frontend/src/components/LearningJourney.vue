<template>
    <div class="bg-slate-100 rounded-md px-10 py-7 my-4">
        <div class="grid grid-cols-2">
            <p class="text-xl font-bold underline underline-offset-8">
                Job Role Name
            </p>
            <button @click="handleEditClick" class="btn btn-circle place-self-end">
                <svg class="w-4 h-4 fill-current" viewBox="0 0 20 20"><path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z"></path></svg>
            </button>
        </div>
        <p class="text-lg font-normal">
            In Progress
        </p>
        <div class="grid grid-cols-3 gap-4 my-4">
            <div v-for="n in 3" class="bg-slate-50 rounded-md px-2 py-2 outline outline-1 outline-slate-400">{{ n }}</div>
        </div>

        <p class="text-lg font-normal ">
            Completed
        </p>

        <div class="grid grid-cols-3 gap-4 my-4">
            <div v-for="n in 2" class="bg-slate-50 rounded-md px-2 py-2 outline outline-1 outline-slate-400">{{ n }}</div>
        </div>

        <div class="flex flex-row items-center w-full gap-4">
            <progress class="progress w-full" value="40" max="100"></progress>
            <p>40%</p>
        </div>
        
    </div>
</template>

<script setup>
function handleEditClick() {
    router.push({
        path: '/editLJ'
    })
}
</script>