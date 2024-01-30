import { TextToSpeechConfig } from '../../../../types/textToSpeech';
export type ProcessedTextToSpeechConfig = {
    lang?: string;
    pitch?: number;
    rate?: number;
    voice?: SpeechSynthesisVoice;
    volume?: number;
};
export declare class TextToSpeech {
    private static readonly LOAD_VOICES_MS;
    static speak(text: string, config: ProcessedTextToSpeechConfig): void;
    static processConfig(config: boolean | TextToSpeechConfig, set: (config: ProcessedTextToSpeechConfig) => void): void;
}
//# sourceMappingURL=textToSpeech.d.ts.map