import { FileAttachments } from '../../../../../types/fileAttachments';
import { MessageFileType } from '../../../../../types/messageFile';
import { DeepChat } from '../../../../../deepChat';
export interface AttachmentObject {
    file: File;
    fileType: MessageFileType;
    attachmentContainerElement: HTMLElement;
    removeButton?: HTMLElement;
}
export declare class FileAttachmentsType {
    private readonly _attachments;
    private readonly _fileCountLimit;
    private readonly _toggleContainerDisplay;
    private readonly _fileAttachmentsContainerRef;
    private readonly _acceptedFormat;
    private _validationHandler?;
    constructor(deepChat: DeepChat, fileAttachments: FileAttachments, toggleContainer: (display: boolean) => void, container: HTMLElement);
    attemptAddFile(file: File, fileReaderResult: string): boolean;
    private static isFileTypeValid;
    static getTypeFromBlob(file: File): MessageFileType;
    private addAttachmentBasedOnType;
    private static createImageAttachment;
    private static createAnyFileAttachment;
    addFileAttachment(file: File, fileType: MessageFileType, attachmentElement: HTMLElement, removable: boolean): AttachmentObject;
    private static createContainer;
    createRemoveAttachmentButton(attachmentObject: AttachmentObject): HTMLDivElement;
    removeAttachment(attachmentObject: AttachmentObject): void;
    getFiles(): {
        file: File;
        type: MessageFileType;
    }[];
    removeAllAttachments(): void;
}
//# sourceMappingURL=fileAttachmentsType.d.ts.map