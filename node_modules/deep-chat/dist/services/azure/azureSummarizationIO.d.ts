import { AzureSummarizationResult, AzureAuthenticationError } from '../../types/azureResult';
import { AzureSummarizationConfig } from '../../types/azure';
import { MessageContentI } from '../../types/messagesInternal';
import { Messages } from '../../views/chat/messages/messages';
import { AzureLanguageIO } from './azureLanguageIO';
import { PollResult } from '../serviceIO';
import { DeepChat } from '../../deepChat';
type RawBody = Required<Pick<AzureSummarizationConfig, 'language'>>;
export declare class AzureSummarizationIO extends AzureLanguageIO {
    url: string;
    textInputPlaceholderText: string;
    private messages?;
    constructor(deepChat: DeepChat);
    preprocessBody(body: RawBody, messages: MessageContentI[]): {
        analysisInput: {
            documents: {
                id: string;
                language: string;
                text: string;
            }[];
        };
        tasks: {
            kind: string;
        }[];
    } | undefined;
    callServiceAPI(messages: Messages, pMessages: MessageContentI[]): Promise<void>;
    extractResultData(result: Response & AzureAuthenticationError): Promise<{
        makingAnotherRequest: true;
    }>;
    extractPollResultData(result: AzureSummarizationResult): PollResult;
}
export {};
//# sourceMappingURL=azureSummarizationIO.d.ts.map