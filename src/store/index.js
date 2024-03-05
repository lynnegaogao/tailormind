import { createStore } from "vuex";

export const store = createStore({
    state: {
        learningPathData: [],
        mindMapData: [],
        submitChatData: [],
        isReflection:false,
    },
    getters: {},
    mutations: {
        SET_SUBMIT_CHAT_DATA(state, data) {
            state.submitChatData = data;
        },
        SET_LEARNING_PATH_DATA(state, data) {
            state.learningPathData = data;
        },
        SET_MIND_MAP_DATA(state, data) {
            state.mindMapData = data;
        }
    },
    actions: {
        submitChatData({ commit }, data) {
            commit('SET_SUBMIT_CHAT_DATA', data);
        },
        learningPathData({ commit }, data) {
            commit('SET_LEARNING_PATH_DATA', data);
        },
        mindMapData({ commit }, data) {
            commit('SET_MIND_MAP_DATA', data);
        }
    },
    modules: {}

});

