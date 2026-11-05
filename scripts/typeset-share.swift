import AppKit
import CoreText
let root=FileManager.default.currentDirectoryPath
func font(_ weight:String,_ size:CGFloat)->NSFont {
 let url=URL(fileURLWithPath:root+"/assets/fonts/lyon-arabic-display-"+weight+".otf")
 CTFontManagerRegisterFontsForURL(url as CFURL,.process,nil)
 let descriptors=CTFontManagerCreateFontDescriptorsFromURL(url as CFURL) as! [CTFontDescriptor]
 let f=CTFontCreateWithFontDescriptor(descriptors[0],size,nil)
 return NSFont(name:CTFontCopyPostScriptName(f) as String,size:size)!
}
let bitmap=NSBitmapImageRep(bitmapDataPlanes:nil,pixelsWide:1200,pixelsHigh:630,bitsPerSample:8,samplesPerPixel:4,hasAlpha:true,isPlanar:false,colorSpaceName:.deviceRGB,bytesPerRow:0,bitsPerPixel:0)!
NSGraphicsContext.saveGraphicsState()
NSGraphicsContext.current=NSGraphicsContext(bitmapImageRep:bitmap)
let image=NSImage(contentsOfFile:root+"/generated_images/exec-81d25570-783f-424a-be86-5d2910ea2dd8.png")!
image.draw(in:NSRect(x:0,y:0,width:1200,height:630))
func text(_ s:String,_ weight:String,_ size:CGFloat,_ y:CGFloat,_ h:CGFloat){
 let p=NSMutableParagraphStyle();p.alignment = .right;p.baseWritingDirection = .rightToLeft
 let a:[NSAttributedString.Key:Any]=[.font:font(weight,size),.foregroundColor:NSColor(red:0.08,green:0.15,blue:0.12,alpha:1),.paragraphStyle:p]
 (s as NSString).draw(in:NSRect(x:720,y:y,width:430,height:h),withAttributes:a)
}
text("راحتهم", "black", 83, 318, 115)
text("مسؤوليتنا.", "black", 83, 223, 115)
text("سكن، نقل وإعاشة.", "bold", 35, 141, 65)
text("مساكن أسبار", "bold", 26, 50, 55)
NSGraphicsContext.restoreGraphicsState()
try bitmap.representation(using:.jpeg,properties:[.compressionFactor:0.9])!.write(to:URL(fileURLWithPath:root+"/assets/share/aspar-social-lyon.jpg"))
print("Created 1200 x 630 social image using original Lyon fonts")
