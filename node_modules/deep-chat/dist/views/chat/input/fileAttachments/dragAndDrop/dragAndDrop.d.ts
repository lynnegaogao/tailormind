import { CustomStyle } from '../../../../../types/styles';
import { FileAttachments } from '../fileAttachments';
export declare class DragAndDrop {
    static create(containerElement: HTMLElement, fileAttachments: FileAttachments, dnd?: boolean | CustomStyle): void;
    private static createElement;
    private static addEvents;
    private static uploadFile;
    private static display;
    private static hide;
    static isEnabled(fileAttachments: FileAttachments, dragAndDrop?: boolean | CustomStyle): boolean;
}
//# sourceMappingURL=dragAndDrop.d.ts.map