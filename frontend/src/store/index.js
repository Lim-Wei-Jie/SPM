import { createStore } from "vuex";
import test from '../store/modules/test'

export const store = createStore({
    modules: {
        test
    }
})

export default store