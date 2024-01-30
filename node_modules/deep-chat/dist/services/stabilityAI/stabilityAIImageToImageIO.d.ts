import { StabilityAITextToImageResult } from '../../types/stabilityAIResult';
import { MessageContentI } from '../../types/messagesInternal';
import { Messages } from '../../views/chat/messages/messages';
import { StabilityAIIO } from './stabilityAIIO';
import { Response } from '../../types/response';
import { DeepChat } from '../../deepChat';
export declare class StabilityAIImageToImageIO extends StabilityAIIO {
    url: string;
    private readonly _imageWeight;
    textInputPlaceholderText: string;
    introPanelMarkUp: string;
    constructor(deepChat: DeepChat);
    private static cleanConfig;
    private static canSendFileTextMessage;
    private createFormDataBody;
    callServiceAPI(messages: Messages, pMessages: MessageContentI[], files?: File[]): Promise<void>;
    extractResultData(result: StabilityAITextToImageResult): Promise<Response>;
}
//# sourceMappingURL=stabilityAIImageToImageIO.d.ts.map