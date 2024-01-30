import { FileAttachments } from '../../../../../types/fileAttachments';
import { ServiceFileTypes } from '../../../../../services/serviceIO';
import { FileAttachmentsType } from './fileAttachmentsType';
import { DeepChat } from '../../../../../deepChat';
export declare class FileAttachmentTypeFactory {
    static create(deepChat: DeepChat, files: FileAttachments, toggleContainer: (display: boolean) => void, container: HTMLElement, type: keyof ServiceFileTypes): FileAttachmentsType;
}
//# sourceMappingURL=fileAttachmentTypeFactory.d.ts.map