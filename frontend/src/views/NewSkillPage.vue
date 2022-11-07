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
                            <RouterLink to="/hr" v-on:click="handleBack()">Skill</RouterLink>
                        </li> 
                        <li>
                            New skill 
                        </li>
                    </ul>
                </div>
    
                <div class="grid grid-cols-2 my-8">
                    <p class="text-3xl"> New Skill </p>
                </div>
    
                <!-- Form component -->
                <form class="form-control space-y-6">
    
                    <!-- skill name input -->
                    <div class="space-y-2">
                        <h3 class="font-medium text-lg">Skill Name</h3>
                        <input type="text" v-model="skillName" placeholder='Enter Skill Name' class="input input-bordered w-3/6 text-2xl">
                    </div>
                    
                    <!-- skill desc input -->
                    <div class="space-y-2 w-4/6">
                        <p class="font-medium text-lg">
                            Skill Description
                        </p>
                        <input type="text" v-model="skillDesc" placeholder='Enter Skill Description' class="input input-bordered w-full">
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
                                    <!-- binding the entire object as each -->
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
                                                        <button class="btn btn-sm btn-error btn-outline w-3/5" type="submit" @click.prevent="confirmAddCourse()">Confirm</button>
                                                        
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
                            <div class="flex justify-evenly" v-for="each of addedCourses" >
                                <div class="text-center bg-gray-800 rounded-lg w-11/12 p-3 relative">
                                    <p class="text-white" >{{ each }}</p> 
                                    <!-- <br> -->
                                    <!-- <p class="text-white"> {{ courseDetail.Course_Desc }}</p>  -->
                                    <!-- Remove course button -->
                                    <label for="remove-modal" class="btn modal-button btn-xs btn-circle btn-error btn-outline absolute right-0 top-0" @click="handleRemoveCourse(each)">
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
                    <label for="create-skill-modal" class="btn w-1/5" type="submit"  v-on:click="handleCreateSkill()">Create Skill</label>
                    <!-- Modal pop-up -->
                    <input type="checkbox" id="create-skill-modal" class="modal-toggle"/>
                                    <label for="create-skill-modal" class="modal cursor-default">
                                        <label class="modal-box relative space-y-8">
                                            <div v-if="noCreateErr">
                                                <p class="text-lg">
                                                    <section class="text-xl mt-3">
                                                        Skill created succesfully
                                                    </section>
                                                </p>   
                                                <!-- Ok button -->
                                                    <div class="grid grid-cols-2 gap-6">
                                                        <RouterLink :to="`/hr`">
                                                            <div class="btn btn-sm flex justify-end">    
                                                                Ok
                                                           </div> 
                                                        </RouterLink>
                                                    </div>
                                            </div>
                                            <div v-if="haveError">
                                                <p class="text-lg">
                                                   <section class="text-xl mt-3">
                                                        {{ error }} 
                                                    </section>    
                                                </p>   
                                            </div>
                                            <div v-else>
                                                <p class="text-lg">
                                                    <div v-for="error of createErrArr">
                                                        <section class="text-xl mt-3">
                                                            {{ error }} 
                                                        </section>
                                                    </div>
                                                    <!-- Reset error msg button -->
                                                    <div class="grid grid-cols-2 gap-6">
                                                        <div class="flex justify-end">
                                                            <div class="btn btn-sm btn-error btn-outline w-3/5" @click="resetError()">
                                                                Ok
                                                            </div>
                                                        </div>
                                                    </div>
                                                </p>   
                                            </div>
                                            
                                        </label>
                                    </label>
                <!--end of modal pop up-->
                    
                    
                    <!-- Cancel button -->
                    <div>
                        <RouterLink :to="`/hr`" v-on:click="handleBack()">
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
    import { useSkillCoursesStore } from '@/store/index.js'
    import { getCoursesBySkill, getAllCourses, createSkill, addCoursesToSkill, getAllSkills } from "@/endpoint/endpoint.js";
    
    
    const router = useRouter()
    const route = useRoute()
    

    const viewAllCourses = ref([])
    const checkedCourses = ref([]) //array of course objects
    const skillName = ref('');
    const skillDesc = ref('');
    const addCourseIDArr = ref([]) //used to call api
    const noCreateErr = ref(true);
    const createErrArr = ref([]);
   

    const removeModal = reactive({
        courseName: '',
        courseID: '', 
        removeCourseID: [] // for API call
    })

    const skillCoursesStore = useSkillCoursesStore()

    // this is an array
    const addedCourses = ref(skillCoursesStore.skillCourses.addedCourses)

    
    const loading = ref(true);
    const error = ref('');
    const haveError = ref(false);

    // reset skillCoursesStore when exit create skill page (using back or cancel btn)
    function handleBack() {
        skillCoursesStore.skillCourses.addedCourses = []
        addedCourses = [];
    }

    function handleRemoveCourse(courseName) {
        removeModal.courseName = courseName
    }
    
    function confirmRemoveCourse(courseName) {
        //console.log(courseName);
        //console.log(addedCourses);
        //console.log(addedCourses.value);
        for(let i = 0; i < addedCourses.value.length; i++){
            //console.log(i);
            if(addedCourses.value[i] === courseName){
                delete addedCourses.value[i];
                addCourseIDArr.value.splice(i);
                //console.log(addCourseIDArr.value);
            }
        }
        // removing skill key from coursesBySkillName object in pinia store only
        //delete store.skill.courses[courseName];
        
        //console.log(removeCourseIDArr);
    
        
    }
    function resetError(){
        createErrArr.value = [];
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
        //this is an array of objects
        //console.log(checkedCourses.value) 
        //after confirm adding a course, need to store in store.skill.courses to display on the ui again    
        for(var checkedCourse of checkedCourses.value){
           
            addedCourses.value.push(checkedCourse.Course_Name.toString());
            addCourseIDArr.value.push(checkedCourse.Course_ID.toString());
            console.log(addCourseIDArr.value);
        }
    }

    async function handleCreateSkill(){
        if(skillName.value.length === 0){
            createErrArr.value.push('Please enter skill name')
            noCreateErr.value = false;
            
        }
        if(skillName.value.length > 60){
            createErrArr.value.push('Skill name is too long, it cannot exceed 60 characters')
            noCreateErr.value = false;
            
        }
        if(skillDesc.value.length === 0){
            createErrArr.value.push('Please enter skill description')
            noCreateErr.value = false;
            
        }
        if(addCourseIDArr.value.length === 0){
            createErrArr.value.push('Please select at least 1 course')
            noCreateErr.value = false;
            
        }
        

        else{
            try {
            //getting the skillID 
            const skillID = ref();
            const skills = await getAllSkills()
            for (var each of skills) {
                if(each.Skill_Name == skillName.value) {
                    skillID.value = each.Skill_ID
                }
            }
            // const skillID = ref();
            // const allSkills = await getAllSkills(); 
            // skillID.value = (allSkills.length) + 1; 

            //first api to update skill name and desc
            const createdSkill = await createSkill(skillName.value, skillDesc.value);

                //second api to update courses added
                //if(addCourseIDArr.value.length > 0){
                    const addCourses = await addCoursesToSkill(skillID.value, addCourseIDArr);
                //}
            
            }
            catch (err) {
                error.value = err;
                console.log(err);
                haveError.value = true;
            }
        }
        
        

    }
    
    </script>
    
    <style scoped>
    </style>