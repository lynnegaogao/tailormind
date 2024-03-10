import { createStore } from "vuex";

export const store = createStore({
    state: {
        learningPathData: [],
        mindMapData: [],
        submitChatData: [],
        isReflection:false,
        cyInstance:{},
        ur:{},
        milestonesByUser:[],
        currentEditNoteNodeId:'',
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
        },
        SET_CY_INSTANCE_DATA(state,data){
            state.cyInstance = data;
        },
        SET_UR_DATA(state,data){
            state.ur = data;
        },
        SET_MILESTONE_BYUSER_DATA(state,data){
            state.milestonesByUser = data;
        },
        SET_CURRENT_EDITNOTE_NODEID_DATA(state,data){
            state.currentEditNoteNodeId = data;
        },
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
        },
        cyInstance({ commit }, data) {
            commit('SET_CY_INSTANCE_DATA', data);
        },
        ur({ commit }, data) {
            commit('SET_UR_DATA', data);
        },
        milestonesByUser({ commit }, data) {
            commit('SET_MILESTONE_BYUSER_DATA', data);
        },
        currentEditNoteNodeId({ commit }, data) {
            commit('SET_CURRENT_EDITNOTE_NODEID_DATA', data);
        },
    },
    modules: {}

});

