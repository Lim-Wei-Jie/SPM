import { ref, reactive, computed } from "vue"
import { defineStore } from 'pinia'

export const useRoleStore = defineStore('role', () => {

    const role = reactive({
        roleName: '',
        roleID: '',
        roleDesc: '',
        coursesBySkillName: {}
        /*
        coursesBySkillName: {
            skillName1: {
                'skillID': '',
                'courses': {
                    courseName1: {courseDetail1},
                    courseName2: {courseDetail2}
                }
            },
        }
        */
    })

    const storeRole = (roleName, roleID, roleDesc, coursesBySkillName) => {
        role.roleName = roleName
        role.roleID = roleID
        role.roleDesc = roleDesc
        role.coursesBySkillName = coursesBySkillName
    }

    return {
        role,
        storeRole
    }

})

export const useAssignSkillsStore = defineStore('assignSkills', () => {

    const assignSkills = reactive({
        removeSkillsIDArr: [],
        addSkillsIDArr: []
    })

    return {
        assignSkills
    }

})

export const useSkillStore = defineStore('skill', () => {

    const skill = reactive({
        skillName: '',
        skillID: '',
        skillDesc: '',
        courses: {}
        /*
        courses: {
            courseName1: {courseDetail1},
            courseName2: {courseDetail2}
        }
        */
    })

    const storeSkill = (skillName, skillID, skillDesc, courses) => {
        skill.skillName = skillName
        skill.skillID = skillID
        skill.skillDesc = skillDesc
        skill.courses = courses
    }

    return {
        skill,
        storeSkill
    }

})

export const useSkillCoursesStore = defineStore('skillCourses', () => {

    const skillCourses = reactive({
        addedCourses: [],
       
    })

    return {
        skillCourses
    }

})
