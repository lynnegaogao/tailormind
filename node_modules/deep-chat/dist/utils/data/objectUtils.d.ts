export declare class ObjectUtils {
    static setPropertyValueIfDoesNotExist<T>(object: T, nestedKeys: string[], value: unknown): void;
    static setPropertyValue<T>(object: T, nestedKeys: string[], value: unknown): void;
    static getObjectValue<T>(object: T, nestedKeys: string[]): object | undefined;
    static overwritePropertyObjectFromAnother<T>(target: T, source: T, nestedKeys: string[]): void;
}
//# sourceMappingURL=objectUtils.d.ts.map