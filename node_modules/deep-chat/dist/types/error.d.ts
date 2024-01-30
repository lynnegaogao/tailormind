export interface ErrorMessageOverrides {
    default?: string;
    service?: string;
    speechToText?: string;
}
export interface ErrorMessages {
    displayServiceErrorMessages?: boolean;
    overrides?: ErrorMessageOverrides;
}
export type OnError = (error: string) => void;
//# sourceMappingURL=error.d.ts.map