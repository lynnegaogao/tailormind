import { Response } from '../../../../types/response';
import { MessagesBase } from '../messagesBase';
export declare class MessageStream {
    static readonly MESSAGE_CLASS = "streamed-message";
    private _streamedContent;
    private _streamType;
    private _elements?;
    private _hasStreamEnded;
    private _activeMessageRole?;
    private readonly _messages;
    private static readonly HTML_CONTENT_PLACEHOLDER;
    constructor(messages: MessagesBase);
    upsertStreamedMessage(response?: Response): void;
    private setInitialState;
    private updateBasedOnType;
    private updateText;
    private updateHTML;
    finaliseStreamedMessage(): void;
}
//# sourceMappingURL=messageStream.d.ts.map