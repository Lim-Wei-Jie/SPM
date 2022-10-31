<template>
    <!-- eslint-disable -->
    <div>
        <NavBar/>
        <div class="container mx-auto my-8">
            <div v-if="loading">
                <!-- Breadcrumbs component -->
                <div class="text-sm breadcrumbs">
                    <ul>
                        <li>
                            <RouterLink to="/login">Home</RouterLink>
                        </li>
                        <li>
                            <RouterLink to="/hr">Skill</RouterLink>
                        </li> 
                        <li>
                            New skill 
                        </li>
                    </ul>
                </div>
    
                <div class="grid grid-cols-2 my-8">
                    <p class="text-3xl"> New Skill </p>
                    <!-- Delete button -->
                    <button @click="deleteSkill(store.skill.skillID)" class="btn btn-circle place-self-end">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
                        </svg>
                    </button>
                </div>
    
                <!-- Form component -->
                <form class="form-control space-y-6" @submit.prevent="handleEditSkill">
    
                    <!-- Role name input -->
                    <div class="space-y-2">
                        <h3 class="font-medium text-lg">Skill Name</h3>
                        <input type="text" v-model="store.skill.skillName" class="input input-bordered w-3/6 text-2xl">
                    </div>
                    
                    <!-- Role desc input -->
                    <div class="space-y-2 w-4/6">
                        <p class="font-medium text-lg">
                            Skill Description
                        </p>
                        <input type="text" v-model="store.skill.skillDesc" class="input input-bordered w-full">
                    </div>
    
                    <!-- Skill courses -->
                    <div class="space-y-3">
                        <p class="font-medium text-lg"> Courses </p>

                        <!--Add course button-->
                        <label for="add-modal" class="btn w-1/5" @click="handleAddCourseClick()">
                            Add Course
                        </label>
                        <!-- Modal pop-up -->
                            <input type="checkbox" id="add-modal" class="modal-toggle"/>
                            <label for="add-modal" class="modal cursor-default">
                                <label class="modal-box relative" for="">
                                    <!-- All the available course names in the form of checkboxes-->
                                    <!-- v-model="checkboxes" -->
                                    <p class="font-medium text-lg">Courses:</p>
                                    <div class="m-4" v-for="each of viewAllCourses" >
                                        <input v-bind:value="each"  class="text-2xl font-bold underline underline-offset-8" type="checkbox"  name='checkbox' v-model="checkedCourses"/>
                                            <label v-bind:for="each.course_id">
                                                {{each.Course_Name}}
                                            </label>
                                    </div> 
                                        
                                            <!-- Confirm + cancel buttons for adding of course(s) -->
                                            <div class="grid grid-cols-2 gap-6">
                                                <div class="flex justify-end">
                                                    <!-- <label for="add-modal" class="btn btn-sm btn-error btn-outline w-3/5" @click="confirmAddCourse(checkedCourses)"> -->
                                                        <button class="btn btn-sm btn-error btn-outline w-3/5" type="submit" @click="confirmAddCourse()">Confirm</button>
                                                        
                                                    <!-- </label> -->
                                                </div>
                                                <div class="flex justify-start">
                                                    <label for="add-modal" class="btn btn-sm btn-outline w-3/5">
                                                        Cancel
                                                    </label>
                                                </div>
                                            </div>
                                </label>
                            </label>
                        
                        <!-- Courses component -->
                        <div class="grid grid-cols-4 gap-6 bg-gray-700 rounded-lg my-6 p-8">
                            <!-- Course -->
                            <div class="flex justify-evenly" v-for="(courseDetail, courseName) in store.skill.courses" >
                                <div class="text-center bg-gray-800 rounded-lg w-11/12 p-3 relative">
                                    <p class="text-white">{{ courseName }}</p> 
                                    <!-- <br> -->
                                    <!-- <p class="text-white"> {{ courseDetail.Course_Desc }}</p>  -->
                                    <!-- Remove course button -->
                                    <label for="remove-modal" class="btn modal-button btn-xs btn-circle btn-error btn-outline absolute right-0 top-0" @click="handleRemoveCourse(courseName)">
                                        <svg class="h-3 w-3" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                                        </svg>
                                    </label>
                                    <!-- Modal pop-up -->
                                    <input type="checkbox" id="remove-modal" class="modal-toggle"/>
                                    <label for="remove-modal" class="modal cursor-default">
                                        <label class="modal-box relative space-y-8">
                                            <p class="text-lg">
                                                Are you sure you want to delete course:
                                                <section class="text-xl mt-3">
                                                    {{ removeModal.courseName }}
                                                </section>
                                            </p>
                                            <!-- Confirm + cancel buttons -->
                                            <div class="grid grid-cols-2 gap-6">
                                                <div class="flex justify-end">
                                                    <label for="remove-modal" class="btn btn-sm btn-error btn-outline w-3/5" @click="confirmRemoveCourse(removeModal.courseName)">
                                                        Confirm
                                                    </label>
                                                </div>
                                                <div class="flex justify-start">
                                                    <label for="remove-modal" class="btn btn-sm btn-outline w-3/5">
                                                        Cancel
                                                    </label>
                                                </div>
                                            </div>
                                        </label>
                                    </label>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Save button -->
                    <button class="btn w-1/5" type="submit"  v-on:click="handleUpdateSkill()">Save Changes</button>
                    <!-- Cancel button -->
                    <div>
                        <RouterLink :to="`/skill/${skillName}`">
                            <div class="btn btn-outline btn-error w-1/5">
                                Cancel
                            </div>
                        </RouterLink>
                    </div>
    
                </form>
    
            </div>
    
            <div v-else-if="error !== ''">
                {{ error }}
            </div>
            
            <div v-else>
                <button class="btn loading">loading</button>
            </div>
    
        </div>
    
    </div>
    
    </template>
    
    <script setup>
    import NavBar from '@/components/Navbar.vue'
    import { reactive, ref } from 'vue'
    import { useRouter, useRoute } from 'vue-router'
    import { useSkillStore } from '@/store/index.js'
    import { getCoursesBySkill, getAllCourses, deleteSkill, updateSkill } from "@/endpoint/endpoint.js";
    
    const router = useRouter()
    const route = useRoute()
    const store = useSkillStore()
    const viewAllCourses = ref([])
    const allCourses = ref()
    const checkedCourses = ref([])
   

    // from params
    const skillName = route.params.skillName
    
    const removeModal = reactive({
        courseName: '',
        courseID: '', 
        removeCourseID: [] // for API call
    })

    const addModal = reactive({
        skillID: store.skill.skillID, // for API call for skill and course assignment 
        skillName: store.skill.skillName, // for API call for skill and course assignment 
        courseName: '',
        courseID: '', 
        addCourseIDArr: [] // for API call for skill and course assignment 
    })
    
    const loading = ref(true);
    const error = ref('');

    
    function handleRemoveCourse(courseName) {
        removeModal.courseName = courseName
    }
    
    function confirmRemoveCourse(courseName) {
        // store course ID/s in an array for API call when submit form
        //const removeCourseID = store.skill.courses[courseName].Course_ID
        //removeModal.removeCourseID.push(courseID.toString())
    
        // removing skill key from coursesBySkillName object in pinia store only
        delete store.skill.courses[courseName]
    }
    
    function handleEditSkill() {
        // API call here
        
    }
    
    function handleDeleteSkill(skillID) {
        console.log(skillID);
    }

    async function handleAddCourseClick() {
        try {
            const allCourses = await getAllCourses()
            //console.log(allCourses)
            for (var each of allCourses) {
                viewAllCourses.value.push(each)
            }
        } 
        catch (err) {
            error.value = err
            console.log(err);
        }
    }

    function confirmAddCourse(){
        //this is an array
        console.log(checkedCourses.value) 
    //after confirm adding a course, need to store in store.skill.courses to display on the ui again    
        for(var checkedCourse of checkedCourses.value){
           console.log(checkedCourse.Course_Name);
           store.skill.courses[checkedCourse.Course_Name] = checkedCourse.Course_Name;
        }
   
       
    }

    async function handleUpdateSkill(){
        try {
        const updatedSkill = await updateSkill(store.skill.skillID, store.skill.skillName, store.skill.skillDesc)
        }
        catch (err) {
            error.value = err
            console.log(err);
        }
        // try {
        // const updatedCoursesToSkill = await updateSkill(store.skill.skillID, store.skill.skillName, store.skill.skillDesc)
        // }
        // catch (err) {
        //     error.value = err
        //     console.log(err);
        // }

    }
    
    
    </script>
    
    <style scoped>
    </style>