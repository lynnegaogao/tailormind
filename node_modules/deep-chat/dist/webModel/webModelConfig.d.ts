declare const _default: {
    model_list: ({
        model_url: string;
        local_id: string;
        model_lib_url: string;
        vram_required_MB: number;
        low_resource_required: boolean;
        required_features?: undefined;
    } | {
        model_url: string;
        local_id: string;
        model_lib_url: string;
        vram_required_MB: number;
        low_resource_required: boolean;
        required_features: string[];
    })[];
    use_web_worker: boolean;
};
export default _default;
//# sourceMappingURL=webModelConfig.d.ts.map