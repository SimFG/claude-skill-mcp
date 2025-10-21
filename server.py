from mcp.server.fastmcp import FastMCP
import os
import frontmatter
from pathlib import Path
# Create an MCP server
mcp = FastMCP("ClaudeSkillMCP")

@mcp.tool()
def get_all_skills() -> list:
    """Get all available skills"""
    # Get skill paths from environment variable
    skill_paths_str = os.environ.get('CLAUDE_SKILL_PATH', '')
    skill_paths = [path.strip() for path in skill_paths_str.split(',') if path.strip()]
    
    skills = []
    
    # Scan each path for SKILL.md files
    for path in skill_paths:
        path_obj = Path(path)
        if not path_obj.exists() or not path_obj.is_dir():
            continue
        
        for skill_file in path_obj.glob('**/SKILL.md'):
            try:
                # Load and parse markdown file with frontmatter
                post = frontmatter.load(str(skill_file))
                metadata = post.metadata
                
                # Create skill object with required fields
                skill_info = {
                    'name': metadata.get('name', 'Unknown'),
                    'description': metadata.get('description', 'No description'),
                    'path': str(skill_file.absolute())
                }
                skills.append(skill_info)
            except Exception as e:
                # Skip files that can't be processed
                continue
    
    return skills


@mcp.tool()
def use_skill(skill_name: str) -> str:
    """Use a specific skill"""
    # Get skill paths from environment variable
    skill_paths_str = os.environ.get('CLAUDE_SKILL_PATH', '')
    skill_paths = [path.strip() for path in skill_paths_str.split(',') if path.strip()]
    
    # Find the SKILL.md file for the specified skill
    for path in skill_paths:
        path_obj = Path(path)
        if not path_obj.exists() or not path_obj.is_dir():
            continue
        
        for skill_file in path_obj.glob('**/SKILL.md'):
            try:
                # Load and parse markdown file with frontmatter
                post = frontmatter.load(str(skill_file))
                metadata = post.metadata
                
                # Check if this is the requested skill
                if metadata.get('name') == skill_name:
                    skill_path = str(skill_file.absolute())
                    description = metadata.get('description', 'No description')
                    
                    # Return the formatted response
                    return f"🔍 Skill Information Query Result:\n" \
                           f"\nSkill Name: {skill_name}\n" \
                           f"File Path: {skill_path}\n" \
                           f"Main Function: {description}\n" \
                           f"\n📋 Usage Guide:\n" \
                           f"Please read the SKILL.md file at the above path to understand the detailed usage methods and parameter requirements of this skill,\n" \
                           f"then follow the documentation instructions to solve your specific problem.\n" \
                           f"\n⚠️ Note:\n" \
                           f"If you encounter file access permission issues when attempting to read the SKILL.md file or other related files,\n" \
                           f"please request the necessary permissions from the user to access the file content."
            except Exception as e:
                # Skip files that can't be processed
                continue
    
    # If skill not found
    return f"Skill named '{skill_name}' not found. Please check if the skill name is correct."

if __name__ == "__main__":
    mcp.run()
