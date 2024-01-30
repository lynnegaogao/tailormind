import { ServiceIO } from '../../../services/serviceIO';
import { Messages } from '../messages/messages';
import { DeepChat } from '../../../deepChat';
export declare class Input {
    readonly elementRef: HTMLElement;
    constructor(deepChat: DeepChat, messages: Messages, serviceIO: ServiceIO, containerElement: HTMLElement);
    private static createPanelElement;
    private createFileUploadComponents;
    private static createUploadButtons;
    private static addElements;
}
//# sourceMappingURL=input.d.ts.map