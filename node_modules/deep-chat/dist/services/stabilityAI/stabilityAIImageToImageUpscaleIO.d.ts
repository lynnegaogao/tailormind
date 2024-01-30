import { StabilityAITextToImageResult } from '../../types/stabilityAIResult';
import { MessageContentI } from '../../types/messagesInternal';
import { Messages } from '../../views/chat/messages/messages';
import { StabilityAIIO } from './stabilityAIIO';
import { Response } from '../../types/response';
import { DeepChat } from '../../deepChat';
export declare class StabilityAIImageToImageUpscaleIO extends StabilityAIIO {
    url: string;
    textInputPlaceholderText: string;
    introPanelMarkUp: string;
    constructor(deepChat: DeepChat);
    private static cleanConfig;
    private static canSendFileMessage;
    private createFormDataBody;
    callServiceAPI(messages: Messages, _: MessageContentI[], files?: File[]): Promise<void>;
    extractResultData(result: StabilityAITextToImageResult): Promise<Response>;
}
//# sourceMappingURL=stabilityAIImageToImageUpscaleIO.d.ts.map