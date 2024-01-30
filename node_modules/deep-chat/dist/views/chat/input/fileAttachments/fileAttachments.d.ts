import { FileAttachments as FileAttachmentsT } from '../../../../types/fileAttachments';
import { FileAttachmentsType } from './fileAttachmentTypes/fileAttachmentsType';
import { ServiceFileTypes } from '../../../../services/serviceIO';
import { CustomStyle } from '../../../../types/styles';
import { DeepChat } from '../../../../deepChat';
import { Demo } from '../../../../types/demo';
export declare class FileAttachments {
    private readonly _fileAttachmentsTypes;
    readonly elementRef: HTMLElement;
    constructor(inputElementRef: HTMLElement, attachmentContainerStyle?: CustomStyle, demo?: Demo);
    addType(deepChat: DeepChat, files: FileAttachmentsT, type: keyof ServiceFileTypes): FileAttachmentsType;
    private createAttachmentContainer;
    private toggleContainerDisplay;
    getAllFileData(): {
        file: File;
        type: import("../../../../types/messageFile").MessageFileType;
    }[] | undefined;
    completePlaceholders(): Promise<void>;
    static addFilesToType(files: File[], fileAttachmentTypes: FileAttachmentsType[]): void;
    addFilesToAnyType(files: File[]): void;
    removeAllFiles(): void;
    getNumberOfTypes(): number;
}
//# sourceMappingURL=fileAttachments.d.ts.map