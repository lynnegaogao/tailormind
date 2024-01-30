import { ValidateInput } from '../../types/validateInput';
import { MessageContent } from '../../types/messages';
import { DeepChat } from '../../deepChat';
export declare class Legacy {
    static checkForContainerStyles(deepChat: DeepChat, containerRef: HTMLElement): void;
    static handleResponseProperty(result: any | Response): any;
    static processInitialMessageFile(message: MessageContent): void;
    static processValidateInput(deepChat: DeepChat): ValidateInput | undefined;
    static processSubmitUserMessage(content: string): {
        text: string;
    };
    static flagHTMLUpdateClass(bubbleElement: HTMLElement): void;
}
//# sourceMappingURL=legacy.d.ts.map