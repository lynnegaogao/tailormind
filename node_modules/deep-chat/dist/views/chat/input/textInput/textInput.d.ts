import { ServiceIO } from '../../../../services/serviceIO';
import { DeepChat } from '../../../../deepChat';
export declare class TextInputEl {
    static TEXT_INPUT_ID: string;
    readonly elementRef: HTMLElement;
    readonly inputElementRef: HTMLElement;
    private readonly _config;
    submit?: () => void;
    constructor(deepChat: DeepChat, serviceIO: ServiceIO);
    private static processConfig;
    private static preventAutomaticScrollUpOnNewLine;
    static clear(inputElement: HTMLElement): void;
    private createInputElement;
    removeTextIfPlaceholder(): void;
    static toggleEditability(inputElement: HTMLElement, isEditable: boolean): void;
    private addEventListeners;
    private onFocus;
    private onBlur;
    private static createContainerElement;
    private onKeydown;
}
//# sourceMappingURL=textInput.d.ts.map