import { AzureTextToSpeechConfig } from '../../types/azure';
import { AzureTextToSpeechResult } from '../../types/azureResult';
import { MessageContentI } from '../../types/messagesInternal';
import { Messages } from '../../views/chat/messages/messages';
import { AzureSpeechIO } from './azureSpeechIO';
import { Response } from '../../types/response';
import { DeepChat } from '../../deepChat';
export declare class AzureTextToSpeechIO extends AzureSpeechIO {
    private static readonly HELP_LINK;
    introPanelMarkUp: string;
    url: string;
    constructor(deepChat: DeepChat);
    preprocessBody(body: AzureTextToSpeechConfig, messages: MessageContentI[]): string | undefined;
    callServiceAPI(messages: Messages, pMessages: MessageContentI[]): Promise<void>;
    extractResultData(result: AzureTextToSpeechResult): Promise<Response>;
}
//# sourceMappingURL=azureTextToSpeechIO.d.ts.map